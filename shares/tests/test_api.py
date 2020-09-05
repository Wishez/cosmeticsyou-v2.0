
from django.test import TestCase
from model_mommy import mommy
from django.urls import reverse
from shares.models import *
import json

class TestSharesAPI(TestCase):
    def setUp(self):
        slug = 'slug'
        content = 'Content.'
        title = 'Title.'
        page_title = 'Page Title'

        self.single_news = mommy.make(
            'shares.News',
            page_title=page_title,
            title=title,
            content=content,
            slug=slug,
        )
        self.news_list = mommy.make(
            'shares.News',
            _quantity=5
        )

    def test_to_get_single_news(self):
        url = reverse('single_news', kwargs={
            "slug": self.single_news.slug
        })

        response = self.client.get(url)
        data = json.loads(response.content)
        status_code = response.status_code

        self.assertEquals(status_code, 200)
        self.assertEquals(data.title, self.single_news.title)
        self.assertEquals(data.page_title, self.single_news.page_title)
        self.assertEquals(data.content, self.single_news.content)


    def test_to_get_list_news(self):
        url = reverse('news')

        response = self.client.get(url)
        data = json.loads(response.content)
        status_code = response.status_code

        self.assertEquals(status_code, 200)
        self.assertEquals(len(data), 6)


