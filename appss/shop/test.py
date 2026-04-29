from django.test import TestCase, SimpleTestCase
from django.test import Client
from django.views.generic import TemplateView
from . import views


# GET Запросы
class HomePageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/'
        client = Client()
        cls.response = client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'home')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, 'shop') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsIndex)

    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def text_base_template_name(self):
        self.assertTemplateUsed(self.response, 'index.html')
    


class ListServicePageGetTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/list_service/'
        client = Client()
        cls.response = client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'list_service')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, 'shop') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListService)  

    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'shop/list_service.html')

    def text_base_template_name(self):
        self.assertTemplateUsed(self.response, 'index.html')
# Если пользователь не зарегистрирован

class FormServicePageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/form_servace/'
        client = Client()
        cls.response = client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code, 302) 

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'form_servace_name')  

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, 'shop')  

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsService)  

    def test_redirect_url(self):
        self.assertRedirects(self.response, '/user/login/?next=/form_servace/')

    def text_base_template_name(self):
        self.assertTemplateUsed(self.response, 'index.html')