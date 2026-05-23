from django.test import TestCase
from django.test import SimpleTestCase,Client
from appss.shop import views
class HomePageGetTests(SimpleTestCase):
    
    @classmethod
    def setUpClass(cls):
        url = '/'
        client = Client()
        cls.response = client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'home')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.__name__, 'view')


class ListServicePageGetTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/list_service/'
        client = Client()
        cls.response = client.get(url) 

    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)
#Если пользователь не заригистрирван
class FormServacePageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        url = '/form_servace/'
        client = Client()
        cls.response = client.get(url) 
    
    def test_url_access(self):
        self.assertEqual(self.response.status_code,302)