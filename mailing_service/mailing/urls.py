from django.urls import path

from . import views
from .views import ConsumerList, ConsumerDetail, MailingList, MailingDetail

app_name = 'mailing'

urlpatterns = [
    path('', views.index, name='index'),
    # Создание записи
    path('mailing/create/', views.mailing_create, name='mailing_create'),
    path('api/consumer/', ConsumerList.as_view()),
    path('api/consumer/<int:pk>/', ConsumerDetail.as_view()),
    path('api/mailing/', MailingList.as_view()),
    path('api/mailing/<int:pk>/', MailingDetail.as_view()),
]
