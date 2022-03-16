from django.db import models
from taggit.managers import TaggableManager


class Mailing(models.Model):
    text = models.TextField(verbose_name='Сообщение')

    start_date = models.DateTimeField(auto_now_add=False,
                                      verbose_name='Время старта')
    finish_date = models.DateTimeField(auto_now_add=False,
                                       verbose_name='Время завершения')


class Customer(models.Model):
    phone_number = models.CharField(max_length=20)
    provider_code = models.CharField(max_length=20)
    tags = TaggableManager()
    time_zone = models.IntegerField()


class Message(models.Model):
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Время отправки')
    is_sent = models.BooleanField()
    mailing = models.ForeignKey(Mailing,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                related_name='messages',
                                verbose_name='Рассылка')
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name='messages',
                                 verbose_name='Пользователь')
