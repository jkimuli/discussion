from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home,board_topics
from .models import Board

# Create your tests here.


class HomeTestCase(TestCase):

    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/forum/')

        self.assertEquals(view.func, home)


class BoardTopicsCase(TestCase):

    def setUp(self):

        Board.objects.create(name='Random', description='Board for any other random discussions')

    def test_board_topics_view_success_status_code(self):

        url = reverse('board_details', kwargs={'name': 'Random'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_details', kwargs={'name': 'Kotlin'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/forum/board/Random')
        self.assertEquals(view.func, board_topics)


