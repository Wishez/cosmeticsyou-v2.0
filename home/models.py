# -*- encoding: utf-8 -*-

import sys
from django.conf import settings

if getattr(settings, 'IS_PRODUCTION', False):
    reload(sys)
    sys.setdefaultencoding('utf-8')

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import pre_save
from .help_parts import variables_text_1, variables_text_2


class Callback(models.Model):
    callback_name = models.CharField(_('ФИО'), max_length=160)
    callback_phone = models.CharField(_('Телефон'), max_length=30)
    callback_message = models.TextField(_('Комментарий'), max_length=250, null=True, blank=True)

    choices = (
        (_('Новый'), 'Новый'),
        (_('Проконсультированный'), 'Проконсультированный'),
    )
    status = models.CharField(
        _('Статус обратного вызова'),
        choices=choices,
        max_length=20,
        default=_('Новый')
    )
    called_at = models.DateTimeField(
        _('Дата заказа обратного вызова'),
        default=timezone.now
    )

    def __str__(self):
        return self.callback_name + '|' + self.callback_phone

    class Meta:
        verbose_name = _('Обратный вызов')
        verbose_name_plural = _('Обратные вызовы')


class Program(models.Model):
    img = models.FileField(upload_to='uploads/program/', verbose_name='Изображение программы', blank=True, null=True)
    title = models.CharField(max_length=350, verbose_name='Заголовок',  blank=True, null=True)
    p = models.CharField(max_length=350, verbose_name='Параграф под заголовком', blank=True, null=True)

    offer_1 = models.CharField(max_length=350, verbose_name='Предложение 1 (под-заголовок)', blank=True, null=True)

    action_1_1 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_1_2 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_1_3 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_1_4 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)

    offer_2 = models.CharField(max_length=350, verbose_name='Предложение (под-заголовок)', blank=True, null=True)

    action_2_1 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_2_2 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_3 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_4 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_5 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_2_6 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_7 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_8 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_9 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_2_10 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_11 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_2_12 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)

    offer_3 = models.CharField(max_length=300, verbose_name='Предложение 3 (под-заголовок)', blank=True, null=True)

    action_3_1 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_3_2 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_3 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_4 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_5 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_3_6 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_7 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_8 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_9 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_3_10 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_11 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_3_12 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)

    offer_4 = models.CharField(max_length=300, verbose_name='Предложение 4 (под-заголовок)', blank=True, null=True)

    action_4_1 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_4_2 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_3 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_4 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_5 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_4_6 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_7 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_8 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_9 = models.CharField(max_length=350, verbose_name='Действие для выполнение', blank=True, null=True)
    action_4_10 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_11 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)
    action_4_12 = models.CharField(max_length=350, verbose_name='Действие для выполнения', blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.save()

    class Meta:
        verbose_name = _('Стартовая программа')
        verbose_name_plural = _('Стартовые программы')


class Slider(models.Model):
    slide_1 = models.FileField(_('Слайд'), upload_to='uploads/slider/', blank=True, null=True)
    slide_2 = models.FileField(_('Слайд'), upload_to='uploads/slider/',  blank=True, null=True)
    slide_3 = models.FileField(_('Слайд'), upload_to='uploads/slider/',  blank=True, null=True)
    slide_4 = models.FileField(_('Слайд'), upload_to='uploads/slider/',  blank=True, null=True)
    slide_5 = models.FileField(_('Слайд'), upload_to='uploads/slider/',  blank=True, null=True)

    def __str__(self):
        return 'Главный слайдер'

    def show(self):
        self.save()

    class Meta:
        verbose_name = _('Слайдер')
        verbose_name_plural = _('Слайды')

class EmailMessagesSetting(models.Model):

    change_registration_status_subject= models.CharField(
        _('Тема'),
        help_text=_(
            variables_text_2
        ),
        max_length=200,
        default='Изменили статус регистрации'
    )
    registered_a = models.TextField(
        _('Сообщение для Зарегистрированного А'),
        max_length=6000,
        help_text=_(
            variables_text_2
        ),
        default=_('Ваш текущий статус регистрации　ー　"Зарегистрированный А".')
    )
    registered_b = models.TextField(
        _('Сообщение для Зарегистрированного Б'),
        max_length=6000,
        help_text=_(
            variables_text_2
        ),
        default=_('Ваш текущий статус регистрации　ー　"Зарегистрированный Б".')
    )
    set_number_consultant_subject = models.CharField(
        _('Новый номер(Тема)'),#сообщения для смены статуса консультанта.
        max_length=200,
        default=_('У вас есть собственный номер консультанта!'),
        help_text=_(
            variables_text_1
        ),
    )
    set_number_consultant_message = models.TextField(
        _('Новый номер(Сообщение)'),#Сообщение для консультната при установке номера консультанату
        max_length=6000,
        help_text=_(
            variables_text_1
        ),
        default=_('{{first_name}}, мы присвоили вам уникальный номер консультанта ー {{consultant_num}}! '
                'Через него вы можете заходить в свою персональную комнату ー {{url_to_personal_room}}.'
                ''
                'С уважением, Администрация!')
    )
    after_register_subject = models.CharField(
        _('Тема'),
        max_length=200,
        help_text=_(
            variables_text_2
        ),
        default=_('Почти зарегистрированы на сайте {{site}}!')

    )
    after_register_message = models.TextField(
        _('Сообщение'),#_('Сообщение на почту для новоприбывшего консультанта'),
        max_length=6000,
        help_text=_(
            variables_text_2
        ),
        default=_('Приветствую, {{fist_name}}!'
                  'Вы зарегистрировались на нашем сайте. Скоро ваша заявка будет обра-'
                  'ботана и вам будет присвоен новый статус регистрации, вместе с уни-'
                  'кальным идентификатором. '
                  'Всю эту информацию мы пришлём на ваш email ー от вас требуется только '
                  'ожидание! '
                  ''
                  'С наилучшими пожеланиями, Администрация.')
    )
    change_number_consultant_subject = models.CharField(
        _('Изменение номера(Тема)'),
        max_length=200,
        help_text=_(
            variables_text_1
        ),
        default=_('Ваш уникальный номер был изменён!')

    )


    change_number_consultant_message = models.TextField(
        _('Изменённый номер(Соббщение)'),#Сообщение для консультанта при смене номера консультаната
        max_length=6000,
        help_text=_(
            variables_text_1
        ),
        default=_('{{first_name}}, вам следует знать, что мы обновили ваш номер консультанта ー {{consultant_num}}. '
                  'Поскольку номер консультанта изменён, также изменился адрес в вашу персональную комнату ー　{{url_to_personal_room}}.'
                  ''
                  'С уважением, Администрация!')
    )

    statuses = (
        (_('Не активная группа'), 'Не активна группа'),
        (_('Активная группа'), 'Активная группа'),
    )
    is_active = models.CharField(
        _('Активация'),
        default=_('Не активная группа'),
        choices=statuses,
        max_length=20,
    )
    def __str__(self):
        if self.is_active == 'Активная группа': return 'Активная'

        return 'Неактивная'
    class Meta:
        verbose_name = _('Email сообщение')
        verbose_name_plural = _('Email сообщения')



def switch_active_custom(sender, instance, **kwargs):

     if instance.is_active == _('Активная группа'):
         customs = sender.objects.all()
         if len(customs):
             for custom in customs:
                 custom.is_active = _('Не активная группа')
                 custom.save()
         instance.is_active = _('Активная группа')

pre_save.connect(switch_active_custom, sender=EmailMessagesSetting)