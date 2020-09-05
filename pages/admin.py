# -*- coding: utf-8 -*-
from myadmin.admin import admin_site
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import *
# Register your models here.

base_settings_page = ('Базовая настройка страницы', {
                'fields': (
                    ('page_title',),
                    ('meta',),
                ),
            },)


@admin.register(HomePage, site=admin_site)
class HomePageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
    )

@admin.register(MediaPage, site=admin_site)
class MediaPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
    )


@admin.register(ContactsPage, site=admin_site)
class ContactsPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('map',),
            ),
        },),
    )

@admin.register(SharesPage, site=admin_site)
class SharesPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Контент страницы', {
            'fields': (
                ('shares',),
            ),
        },),
    )

@admin.register(RegistrationPage, site=admin_site)
class RegistrationPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
        ('Настройка отправки сообщений', {
            'fields': (
                ('account_sid',),
                ('auth_token',),
                ('phone_from',),
                ('phones_to',),
                ('message',),
            ),
        },),
    )
@admin.register(BusinessPage, site=admin_site)
class BusinessPageAdmin(SingleModelAdmin):
    fieldsets = (
        base_settings_page,
    )
# @admin.register(SharePage)
# class SaunaPageAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     list_display = ('name', 'gallery',)
#     filter_fields = ('name', 'gallery', )
#     search_fields = ('name', 'gallery',)
#     prepopulated_fields = {'slug': ('title',)}
#     # filter_horizontal = ('schedule', 'services',)
#     fieldsets = (
#         base_settings_page,
#         ('Контент страницы', {
#             'fields': (
#                 ('name', 'slug',),
#                 ('services'),
#                 ('schedule'),
#                 ('gallery',),
#                 ('content',),
#             ),
#         },),
#     )


@admin.register(Settings, site=admin_site)
class SettingsAdmin(SingleModelAdmin):
    fieldsets = (
        ('Настройка информации сайта', {
            'fields': (
                ('widgets',),
                ('meta',)
            ),
        },),
        ('Настройка контактной информации', {
            'fields': (
                ('email', 'phone',),
                ('city', 'address',),
                ('addressHref',),
            ),
        },),
    )
