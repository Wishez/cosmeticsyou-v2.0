
from django.test import TestCase
from model_mommy import mommy
from django.urls import reverse
from shares.models import *


class TestSharesAPI(TestCase):
    def setUp(self):
        self.quantity = 42
        self.images_list = mommy.make(
            'album.AlbumImage',
            # _optional_fill=True,
            _quantity=self.quantity
        )


    def test_to_get_list_news(self):
        url = reverse('images_list')
        response = self.client.get(url)

        self.assertEquals(self.quantity, len(response.body))