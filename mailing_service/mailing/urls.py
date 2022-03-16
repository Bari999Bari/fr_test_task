from django.urls import path

from . import views

app_name = 'mailing'

urlpatterns = [
    path('', views.index, name='index'),
    # Создание записи
    path('mailing/create/', views.mailing_create, name='mailing_create'),
]
