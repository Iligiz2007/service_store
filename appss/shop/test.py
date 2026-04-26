from django.test import TestCase
from django.test import SimpleTestCase

#GET Запросы
class HomePageGetTests(SimpleTestCase):
    def test_url_access(self):
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200) 

class ListServicePageGetTests(TestCase):
    def test_url_access(self):
        url = '/list_service/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

#Если пользователь не заригистрирван
class FormServacePageGetTests(SimpleTestCase):
    def test_url_access(self):
        url = '/form_servace/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)