from django.urls import path

from . import views
from .views import ConsumerListView, ConsumerCreateView

app_name = 'mailing'

urlpatterns = [
    path('', views.index, name='index'),
    # Создание записи
    path('mailing/create/', views.mailing_create, name='mailing_create'),
    path('api/consumer/', ConsumerListView.as_view(), name='mailing_create'),
    path('api/consumer/create/', ConsumerCreateView.as_view()),
]
