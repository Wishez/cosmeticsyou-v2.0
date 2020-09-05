# -*- encoding: utf-8 -*-
from django import forms

from .models import User, RefferalConsultant
# Create your models here.
class BaseRegistrationForm(forms.ModelForm):
    # Excluded fields
    # 'street', 'num_home',
    # 'num_apartment', 'passport_data'
    class Meta:
        fields = ('last_name', 'first_name', 'middle_name',
                  'birthday',
                  'phone_number', 'email',
                  'city', 'street', 'region', 'num_home',
                  'num_apartment',)
        widgets = {
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Иванов',
                'pattern': '\D+',
                'autofocus': 'true',
                'class': 'controller__input controller__input_purple child materialShadow',
                #'autocomplete': "last_name",
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Иван',
                'pattern': '([А-Я]|[A-Z])([а-я]+|[a-z]+)(([-\s])([А-Я]|[A-Z])?([а-я]+|[a-z]+))?',
                'class': 'controller__input controller__input_purple child materialShadow',
                #'autocomplete': "first_name",
            }),
            'middle_name': forms.TextInput(attrs={
                'placeholder': 'Иванович',
                'pattern': '([А-Я]|[A-Z])([а-я]+|[a-z]+)',
                'class': 'controller__input controller__input_purple child materialShadow',
                #'autocomplete': "middle_name",
            }),
            'birthday': forms.DateInput(attrs={
                'placeholder': '01/01/1900',
                'type': 'date',
                'class': 'controller__input controller__input_purple child materialShadow',
                'autocomplete': "birthday"
            }),
            # 'passport_data': forms.TextInput(attrs={
            #     'placeholder': '0000-000000',
            #     'class': 'controller__input controller__input_purple child materialShadow',
            # }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+7 (555) 555-35-55',
                'type': 'tel',
                'class': 'controller__input controller__input_purple child materialShadow',
                "maxlength": "30",
                'autocomplete': "phone"
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your_email@mail.ru',
                'class': 'controller__input controller__input_purple child materialShadow',
                #'autocomplete': "email"
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Москва; Стамбул; Лондон',
                'pattern': '\D+',
                'class': 'controller__input controller__input_purple child materialShadow',
                'autocomplete': "city",
            }),
            'region': forms.TextInput(attrs={
                'placeholder': '1239876',
                'pattern': '[0-9\-]*',
                'class': 'controller__input controller__input_purple child materialShadow',
                'autocomplete': "region",
            }),
            'street': forms.TextInput(attrs={
                'placeholder': 'Тисовая; Бейкер-стрит',
                'pattern': '\D+',
                'class': 'controller__input controller__input_purple child materialShadow',
            }),
            'num_home': forms.TextInput(attrs={
                'placeholder': '10A; 11',
                'class': 'controller__input controller__input_small controller__input_purple child materialShadow',
            }),
            'num_apartment': forms.NumberInput(attrs={
                'placeholder': '322',
                'max': 999,
                'min': 1,
                'value': 1,
                'step': 1,
                'class': 'controller__input controller__input_small controller__input_purple child materialShadow',
            }),

        }

class RegistrationConsultantForm(BaseRegistrationForm):
    class Meta(BaseRegistrationForm.Meta):
        model = User


class RegistrationRefferalConsultantForm(forms.ModelForm):
    class Meta(BaseRegistrationForm.Meta):
        model = RefferalConsultant
