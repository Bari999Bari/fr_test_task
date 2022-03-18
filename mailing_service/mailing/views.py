from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
import requests

from .forms import MailingForm
from .models import Mailing, Consumer, Message
from .serializers import ConsumerSerializer, MailingSerializer


def index(request):
    template = 'mailing/index.html'
    mailing_list = Mailing.objects.all()
    paginator = Paginator(mailing_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)


def mailing_create(request):
    # Проверяем, получен POST-запрос или какой-то другой:
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.save()
            return redirect('mailing:index')
        return render(request, 'mailing/create_mailing.html', {'form': form})
    form = MailingForm()
    context = {
        'form': form
    }
    return render(request, 'mailing/create_mailing.html', context)


# DRF


class ConsumerList(generics.ListCreateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class ConsumerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class MailingList(generics.ListCreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        # Работу со временем я не стал пробовать,
        # потому что как сделать чтобы запрос ожидал не знаю вообще,
        # наверное это что-то связанное с ассинхроностью, тьма
        # сделал отправку запроса как смог.
        # Со статистико тоже мало что понял
        for m_id in serializer.data.get('messages'):
            message_to_send = Message.objects.get(id=m_id)
            if not message_to_send.is_sent:
                data = {
                    "id": m_id,
                    "phone": int(message_to_send.consumer.phone_number),
                    "text": serializer.data.get('text'),
                }
                response = requests.post(f'https://probe.fbrq.cloud/v1/send/{m_id}', json=data, headers={
                    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Nzg5NjU0ODUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkJhcmkifQ.rADn5-Eg7EipxwlGyQ5RimDUzJU3pKjFNIn7SITaBGo'
                })
                if response.status_code == 200:
                    message_to_send.is_sent = True
                    message_to_send.save()
        return Response(status=201)


class MailingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
