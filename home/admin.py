# -*- encoding: utf-8 -*-
from myadmin.admin import admin_site
from django.contrib import admin
from .models import *
# Register your models here.

class CallbackAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('callback_name', 'callback_phone','status', 'called_at',)
    filter_fields = ('callback_name', 'status', 'called_at',)
    search_fields = (
        'callback_name', 'callback_phone', 'status', 'called_at',
    )
class EmailAdmin(admin.ModelAdmin):
    list_per_page = 10
    #list_display = ('is_active',)
    fieldsets = (
        ('Активация', {
            'fields': (
                ('is_active',),
            ),
        }),
        ('Статус регисрации консультанта', {
            'fields': (
                ('change_registration_status_subject'),
                ('registered_a'),
                ('registered_b'),
            ),
        }),
        ('Номер консультанта', {
            'fields': (
                ('set_number_consultant_subject'),
                ('set_number_consultant_message'),
                ('change_number_consultant_subject'),
                ('change_number_consultant_message'),
            ),
        }),
        ('Регистрации консультанта', {
            'fields': (
                ('after_register_subject'),
                ('after_register_message'),
            ),
        }),


    )
admin_site.register(Program)
admin_site.register(Slider)
admin_site.register(EmailMessagesSetting, EmailAdmin)
admin_site.register(Callback, CallbackAdmin)
