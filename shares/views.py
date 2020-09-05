# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import  Share
from pages.views import BaseView, SharesPage

# Create your views here.
class SharesView(BaseView):
    template_name = 'shares.html'

    def set_additional_context(self, context):
        context['shares'] = SharesPage.objects.get().shares.all()

        return context

    def __init__(self):
        super(SharesView, self).__init__()
        self.page_model = SharesPage
        self.active_page = 'shares'


class SingleShareView(BaseView):
    template_name = 'share_details.html'

    def __init__(self):
        super(SingleShareView, self).__init__()
        self.is_single_model = False

    def set_additionl_context(self, context):
        context['title'] = self.page.page_title

        return context
    def get(self, request, slug):
        self.page = get_object_or_404(Share, slug=slug)

        return super(SingleShareView, self).get(request)
