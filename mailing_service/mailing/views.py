from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import MailingForm
from .models import Mailing, Consumer
from .serializers import ConsumerListSerializer, ConsumerCreateSerializer


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
class ConsumerListView(APIView):
    """Displaying a list of consumers."""

    def get(self, request):
        consumers = Consumer.objects.all()
        serializer = ConsumerListSerializer(consumers, many=True)
        return Response(serializer.data)


class ConsumerCreateView(APIView):
    """Create consumer."""

    def post(self, request):
        consumer = ConsumerCreateSerializer(data=request.data)
        if consumer.is_valid():
            consumer.save()
        return Response(status=201)
