from django.contrib import admin

from .models import Mailing, Consumer, Message

admin.site.register(Mailing)
admin.site.register(Consumer)
admin.site.register(Message)
