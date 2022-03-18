from django.db import models
from taggit.managers import TaggableManager

from .validators import validate_phone_number


class Consumer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number])
    # Плохое представление о трех полях ниже и их своиствах и назначения
    provider_code = models.CharField(max_length=20)
    tags = TaggableManager()
    time_zone = models.IntegerField()

    def __str__(self):
        return self.name


class Message(models.Model):
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Время отправки')
    is_sent = models.BooleanField()
    consumer = models.ForeignKey(Consumer,
                                 on_delete=models.CASCADE,
                                 related_name='messages',
                                 verbose_name='Пользователь')

    def __str__(self):
        return f'Message id={self.pk} to {self.consumer.name}'


class Mailing(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(verbose_name='Сообщение')
    start_date = models.DateTimeField(auto_now_add=False,
                                      verbose_name='Время старта')
    finish_date = models.DateTimeField(auto_now_add=False,
                                       verbose_name='Время завершения')
    messages = models.ManyToManyField(Message,
                                      blank=True,
                                      null=True,
                                      related_name='mailings',
                                      verbose_name='Сщщбщения')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
