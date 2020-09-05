# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from .models import *
from home.forms import CallbackForm
from django.contrib.sites.models import Site
from home.models import *

def get_single_model(Model):
    return Model.objects.get()

class Activate(TemplateView):
    template_name = 'google80a1baa45799ef98.html'
class BaseView(TemplateView):
    def __init__(self):
        self.page_model = None
        self.page = None
        self.settings = get_single_model(Settings)
        self.meta = self.settings.meta
        self.active_page = ''
        self.is_single_model = True

    # Дополняет контекст свойствами нужной страницы, если нужно
    def set_additional_context(self, context):
        return context
    def get_page(self):
        self.page = self.page_model.objects.get()

    def get_page_context(self, context):
        page = self.page
        # Установка мета-описания для текущей страницы
        if page.meta != '':
            self.meta = page.meta

        context['title'] = page.page_title
        context['page'] = page

        return context

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        if self.is_single_model:
            self.get_page()

        is_page_set = self.page is not None

        if is_page_set:
            page = self.page
            context['title'] = page.page_title
            context['page'] = page
            # Установка мета-описания для текущей страницы
            if page.meta != '':
                self.meta = page.meta

        callback = CallbackForm()

        context['active_page'] = self.active_page
        context['site'] = Site.objects.get_current().domain
        context['callback'] = callback
        context['meta'] = self.meta
        context['settings'] = self.settings

        return self.set_additional_context(context)

class HomeView(BaseView):
    template_name = 'index.html'

    def __init__(self):
        super(HomeView, self).__init__()
        self.page_model = HomePage
        self.active_page = 'home'

class MediaView(BaseView):
    template_name = 'media.html'

    def __init__(self):
        super(MediaView, self).__init__()
        self.page_model = MediaPage
        self.active_page = 'media'
class BusinessView(BaseView):
    template_name = 'business.html'

    def __init__(self):
        super(BusinessView, self).__init__()
        self.page_model = BusinessPage
        self.active_page = 'business'

class ContactsView(BaseView):
    template_name = 'contacts.html'

    def __init__(self):
        super(ContactsView, self).__init__()
        self.page_model = ContactsPage
        self.active_page = 'contacts'
