from django.contrib import admin

from .models import Consumer, Message, Mailing


class ConsumerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'phone_number',
        'provider_code',
        'time_zone',
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'create_date',
        'is_sent',
        'consumer',
    )


class MailingAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'start_date',
        'finish_date',
    )


admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Mailing, MailingAdmin)
