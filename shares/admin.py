# -*- coding: utf-8 -*-
from myadmin.admin import admin_site
from django.contrib import admin
from .models import Share, News
from redactor.widgets import AdminRedactorEditor
from django.db import models

@admin.register(Share, site=admin_site)
class AdminShare(admin.ModelAdmin):
    list_per_page = 6
    list_display = ('page_title', 'title', 'published_date', 'created_date',)
    filter_fields = ('page_title', 'title', 'published_date', 'created_date',)
    search_fields = ('page_title', 'title', 'published_date', 'created_date',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    prepopulated_fields = {'slug': ('page_title',)}
    fieldsets = (
        ('Базовая настройка страницы акции', {
            'fields': (
                ('page_title', 'slug',),
                ('meta',),
            ),
        },),
        ('Контент страницы', {
            'fields': (
                ('title',),
                ('announce',),
                ('additional_text'),
            ),
        },),
        ('Публикация', {
            'fields': (
                ('published_date',),
            ),
        },),
        ('Медиа', {
            'fields': (
                ('img',),
                ('image', 'image_1',),
                ('image_2', 'image_3',),
            ),
        },),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminRedactorEditor},
    }

@admin.register(News, site=admin_site)
class AdminNews(admin.ModelAdmin):
    list_per_page = 6
    list_display = ('page_title', 'title', 'created_at', 'is_shown',)
    filter_fields = ('page_title', 'title', 'created_at',)
    search_fields = ('page_title', 'title', 'created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('page_title',)}
    fieldsets = (
        ('Базовая настройка страницы акции', {
            'fields': (
                ('page_title', 'slug',),
                ('meta',),
                ('is_shown',),
            ),
        },),
        ('Контент страницы', {
            'fields': (
                ('title',),
                ('announce',),
                ('content',),
            ),
        },),
        ('Медиа', {
            'fields': (
                ('preview', 'album',),
            ),
        },),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminRedactorEditor},
    }
