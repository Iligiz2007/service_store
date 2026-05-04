from django.test import TestCase, SimpleTestCase
from django.test import Client
from django.urls import reverse
from django.views.generic import TemplateView
from . import views
from .models import Service
from appss.user.models import User
from .forms import FormService
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

    def test_base_template_name(self):
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


#Тест моделей
class ServiceModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'

        )

    def setUp(self):
        self.service = Service(
            title = 'Создание ботов',
            description = 'Я могу создавать ботов в max и telegram',
            price = 100,
            user = self.user
        )
    def test_create_service(self):
        self.assertIsInstance(self.service,Service)
    
    def test_title_Service(self):
        self.assertEqual(str(self.service),'Создание ботов')
    def test_saving_and_retrieving_service(self):
        first_service = Service()
        first_service.title = 'Первая услуга'
        first_service.description = 'Описание первой услуги'
        first_service.price = 155
        first_service.user = self.user
        first_service.save()

        second_service = Service()
        second_service.title = 'second услуга'
        second_service.description = 'Описание second услуги'
        second_service.price = 100
        second_service.user = self.user
        second_service.save()

        all_service = Service.objects.all()
        self.assertEqual(all_service.count(),2)

        first_saved_service = all_service[0]
        first_saved_service = all_service[1]
        self.assertEqual(first_saved_service.title,'second услуга')
        self.assertEqual(first_saved_service.user, self.user)
#Тесты для форм
class ServiceFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'

        )
    def setUp(self):
        self.client.login(username='Ivan', password='lollol212')
        url = reverse('shop:form_servace_name')
        self.response  = self.client.get(url)

    def test_service_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,FormService)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_bootstrap_class_used_for_default_styling(self):
    # Для твоей формы (FormService) - исправлено имя
        self.assertContains(self.response, 'class="form-control"')
    
    def test_book_form_validation_for_blank_items(self):
        add_sevice_form = FormService(data={'title':'','description':'','price':''})
        self.assertFalse(add_sevice_form.is_valid())