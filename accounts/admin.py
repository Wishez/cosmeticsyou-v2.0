# -*- coding: utf-8 -*-
from django.contrib import admin
from myadmin.admin import admin_site
from .models import *

class ConsultantAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('last_name', 'first_name', 'consultant_num', 'phone_number', 'email', 'status', 'refferal_url', 'url_to_personal_room',)
    # date_hierarchy = 'last_name'
    list_filter = ('status', 'last_name', 'first_name', 'middle_name', 'citizenship', 'city', 'region',)
    filter_horizontal = ('user_lead', 'user_lead_1', 'user_lead_2',)
    search_fields = (
        'last_name',
        'first_name',
        'middle_name',
        'city',
        'region',
        'consultant_num',
        'passport_data',
        'birthday',
        'street',
        'num_home',
        'num_apartment',
        'email',
        'phone_number',
        'user_led',
        'user_led_1',
        'user_led_2',
    )
    fieldsets = (
        ('Персональные данные', {
            'fields': (
                ('email',),
                ('last_name',),
                ('first_name',),
                ('middle_name',),
                # ('passport_data',),
                ('birthday',),
                ('phone_number',),
                ('citizenship',),
            ),
        },),
        ('Адрес', {
            'fields': (
                ('region',),
                ('city',),
                ('street',),
                ('num_home',),
                ('num_apartment',),
            ),
        },),
        ('Технические данные', {
            'fields': (
                ('consultant_num', 'status',),
            ),
        },),
        ('Рферальные данные', {
            'fields': (
                ('refferal_url','url_to_personal_room',),
                ('user_led', 'user_led_1', 'user_led_2',),
            ),
        },),
        ('Списки рефералов консультанта', {
            'fields': (
                ('user_lead',), ('user_lead_1',), ('user_lead_2',),
            ),
        },),
    )

class RelatedConsultantAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('last_name', 'first_name',  'middle_name', 'consultant_num', 'refferal_url', 'url_to_personal_room', 'email',)
    list_filter = ('last_name', 'first_name', 'middle_name', 'consultant_num',)
    filter_horizontal = ('user_lead', 'user_lead_1', 'user_lead_2',)
    search_fields = (
        'last_name',
        'first_name',
        'middle_name',
        'email',
        'user_led',
        'user_led_1',
        'user_led_2',
    )
    fieldsets = (
        ('Персональная данные', {
            'fields': (
                ('email',),
                ('last_name',),
                ('first_name',),
            ),
        },),
        ('Технические данные', {
            'fields': (
                ('consultant_num', 'status',),
            ),
        },),
        ('Рферальные данные', {
            'fields': (
                ('refferal_url', 'url_to_personal_room',),
                ('user_led', 'user_led_1', 'user_led_2',),
            ),
        },),
        ('Списки рефералов консультанта', {
            'fields': (
                ('user_lead',), ('user_lead_1',), ('user_lead_2',),
            ),
        },),
    )
# Register your models here.

admin_site.register(User, ConsultantAdmin)
admin_site.register(RefferalConsultant, ConsultantAdmin)
admin_site.register(RelatedConsultant, RelatedConsultantAdmin)