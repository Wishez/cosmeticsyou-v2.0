# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from pages.validators import validate_slug_field
from pages.models import BasePage, TimeStampedModel
import uuid as uuid_lib



class Item(TimeStampedModel):
    # imte_image =
    class Meta:
        db_table = 'Предмет'

class Share(BasePage):
    title = models.CharField(max_length=250, verbose_name="Название акции")
    img = models.FileField(
        upload_to='shares/',
        blank=True,
        null=True,
        verbose_name="Главное Изображение",
        help_text=_('Путь к изображению /media/shares/ на сервере.')
    )

    image = models.FileField(
        upload_to='shares/',
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text=_('Путь к изображению /media/shares/ на сервере.')
    )

    image_1 = models.FileField(
        upload_to='shares/',
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text=_('Путь к изображению /media/shares/ на сервере.')
    )
    image_2 = models.FileField(
        upload_to='shares/',
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text=_('Путь к изображению /media/shares/ на сервере.')
    )
    image_3 = models.FileField(
        upload_to='shares/',
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text=_('Путь к изображению /media/shares/ на сервере.')
    )

    text = models.TextField(blank=True, null=True, verbose_name="Параграф")

    slug = models.SlugField(
        _('Название ссылки к странице акции'),
        help_text=_('К примеру, "new-share-for_2018"'),
        max_length=150,
        validators=[validate_slug_field],
        blank=True,
        null=True
    )
    additional_text = models.TextField(
        _('Контент'),
        max_length=16384, blank=True, null=True)
    announce = models.TextField(
        _('Анонс акции'),
        max_length=560,
        blank=True,
        null=True
    )

    created_date = models.DateTimeField(
        _('Дата создания'),
        auto_now=True
    )

    published_date = models.DateTimeField(
        _('Дата публикации'),
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = _('Акция')
        verbose_name_plural = _('Акции')
        ordering = ['-published_date']

    def publish(self):
        self.published_date= timezone.now()
        self.save()

    def __str__(self):
        return self.title


class News(BasePage):
    title = models.CharField(max_length=250, verbose_name="Название новости")
    preview = models.ForeignKey(
        "album.AlbumImage",
        blank=True,
        null=True,
        verbose_name="Главное Изображение"
    )
    album = models.ForeignKey(
        "album.Album",
        blank=True,
        null=True,
        verbose_name="Альбом с изображениями"
    )
    slug = models.SlugField(
        _('Название ссылки к странице акции'),
        help_text=_('К примеру, "new-share-for_2018"'),
        max_length=150,
        validators=[validate_slug_field],
        blank=True,
        null=True
    )
    content = models.TextField(
        _('Контент'),
        max_length=16384, blank=True, null=True)
    announce = models.TextField(
        _('Анонс'),
        max_length=560,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True
    )
    is_shown = models.BooleanField(_('Отобразить новость?'), default=True)
    uuid = models.UUIDField(
        _('Идентификатор новости'),
        db_index=True,
        default=uuid_lib.uuid4,
        editable=True
    )

    class Meta:
        db_table = 'consultant_news'
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        ordering = ['-created_at']

    def __str__(self):
        return self.title




