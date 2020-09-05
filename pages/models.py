# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from home.help_parts import variables_text_2


class Settings(TimeStampedModel):
    name = models.CharField(
        _('Имя настройки'),
        max_length=100,
        default='Глобальная настройка'
    )
    widgets = models.TextField(
        _('Метрики, виджеты и прочее'),
        max_length=8196,
        blank=True,
        null=True
    )
    meta = models.TextField(
        _('Глобальное META-описание сайта'),
        max_length=300,
        blank=True,
        null=True
    )
    email = models.CharField(
        _('Email'),
        max_length=200,
        blank=True,
        null=True,
        default='support@cosmeticsyou.ru'
    )
    phone = models.CharField(
        _('Телефон'),
        max_length=90,
        blank=True,
        null=True,
        default='+7 (965) 158-14-81'
    )
    city = models.CharField(
        _('Город'),
        max_length=100,
        blank=True,
        null=True,
        default='г. Москва'
    )
    address = models.CharField(
        _('Адрес'),
        max_length=200,
        blank=True,
        null=True,
        default='Ивантеевская д. 13 кор.1'
    )
    addressHref = models.CharField(
        _('Ссылка перенаправляющая на карты(Google/Yandex)'),
        max_length=500,
        blank=True,
        null=True,
        default="https://www.google.ru/maps/place/Ivanteevskaya+ul.,+13%D0%BA1,+Moskva,+107150/@55.818067,37.7239063,17z/data=!3m1!4b1!4m5!3m4!1s0x46b53450cf0645b9:0x869f26e9d7ad24d3!8m2!3d55.818067!4d37.726095?sa=X&ved=0ahUKEwi_jtfNru3SAhWkE5oKHSiQDNYQ8gEIHjAA"
    )

    class Meta:
        db_table='site_settings'
        verbose_name = _('Настройка')
        verbose_name_plural = _('Настройки')


class PageManager(models.Manager):
    user_for_related_fields = True

class BasePage(TimeStampedModel):
    page_title = models.CharField(
        _('Заголовок'),
        help_text=_('Название страницы во вкладке'),
        max_length=100,
        blank=True,
        null=True
    )
    meta = models.TextField(
        _('META-описание страницы'),
        max_length=300,
        blank=True,
        null=True
    )

    objects = PageManager()
    def __str__(self):
        return self.page_title
    class Meta:
        abstract=True

class HomePage(BasePage):

    class Meta:
        db_table='data_home_page'
        verbose_name=_('Страница "Главная"')
        verbose_name_plural = _('Страница "Главная"')


class MediaPage(BasePage):

    class Meta:
        db_table = 'data_Media_page'
        verbose_name = _('Станица "Видео"')
        verbose_name_plural = _('Страница "Видео"')


class SharesPage(BasePage):
    shares = models.ManyToManyField(
        "shares.share",
        verbose_name=_('Акции'),
        related_name='shown_prices_sauna',
        help_text=_('Акции, которые будут отображаться на странице "Акции".'),
        blank=True
    )

    class Meta:
        db_table = 'data_prices_page'
        verbose_name = _('Страница "Акции"')
        verbose_name_plural = _('Страница "Акции"')


class ContactsPage(BasePage):
    map = models.TextField(
        _('Окно с картой'),
        help_text=_('Карта, которая отображается в контактах'),
        max_length=2048,
        blank=True,
        null=True,
        default='<iframe class="map__item"  src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d8966.279574741344!2d37.726095!3d55.818067!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b53450cf0645b9%3A0x869f26e9d7ad24d3!2z0JjQstCw0L3RgtC10LXQstGB0LrQsNGPINGD0LsuLCAxM9C6MSwg0JzQvtGB0LrQstCwLCDQoNC-0YHRgdC40Y8sIDEwNzE1MA!5e0!3m2!1sru!2sru!4v1490693223242" frameborder="0" allowfullscreen></iframe>'
    )

    class Meta:
        db_table = 'data_contacts_page'
        verbose_name = _('Страница "Контакты"')
        verbose_name_plural = _('Страница "Контакты"')

class BusinessPage(BasePage):

    class Meta:
        db_table = 'data_business_page'
        verbose_name = _('Страница "Бизнес"')
        verbose_name_plural = _('Страница "Бизнес"')

class RegistrationPage(BasePage):
    phone_from = models.CharField(
        _('Телефон для отправки сообщений'),
        max_length=20,
        blank=True,
        null=True,
        default="+17609068017"
    )
    phones_to = models.TextField(
        _('Телефоны для отправления сообщений'),
        max_length=1000,
        blank=True,
        null=True,
        default="+79859051251",
        help_text='Указывайте телефоны через запятую +7000999222,+7222111333'
    )
    message = models.TextField(
        _('Опциональное сообщение'),
        max_length=1000,
        blank=True,
        null=True,
        default="Панель администрирования пополнилась новым консультаном!",
        help_text=variables_text_2
    )
    account_sid = models.CharField(
        _('Account Sid'),
        max_length=350,
        blank=True,
        null=True,
        default="",
        help_text="Account Sid из аккаунта TwilioAPI"
    )
    auth_token = models.CharField(
        _('Auth Token'),
        max_length=350,
        blank=True,
        null=True,
        default="",
        help_text="Auth Token из аккаунта TwilioAPI"
    )

    class Meta:
        db_table = 'data_registration_page'
        verbose_name = _('Страница "Регистрация"')
        verbose_name_plural = _('Страница "Регистрация"')