from model_mommy import mommy
from django.test import TestCase
from django.utils.timezone import now

class TestNews(TestCase):
    def setUp(self):
        pass

    def test_to_create_single_news(self):
        title = 'TDD'
        announce = 'TDD is useful the concept of developing a software.'
        content = 'You need write tests before you will use the code, and after to integrate it into codebase. You need check tests, after that, you modify your codebase.'
        slug='make-tdd'
        page_title="TDD is awesome"

        news = mommy.make(
            'shares.News',
            title=title,
            announce=announce,
            content=content,
            slug=slug,
            page_title=page_title
        )

        self.assertEqual(title, news.title)
        self.assertEqual(slug, news.slug)
        self.assertEqual(content, news.content)
        self.assertEqual(announce, news.announce)


