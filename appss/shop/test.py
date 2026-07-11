from django.test import TestCase, SimpleTestCase
from django.test import Client
from django.urls import reverse
from django.views.generic import TemplateView
from . import views
from .models import Service, Task
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
    # Model Service
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


    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.client.login(username='Ivan', password='lollol212')
        url = '/list_service_my/'
        cls.response = cls.client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)


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
        add_service_form  = FormService(data={'title':'','description':'','price':''})
        self.assertFalse(add_service_form .is_valid())


class ServiceUpdateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'

        )

    def setUp(self):
        self.service = Service.objects.create(
            title = 'Создание ботов',
            description = 'Я могу создавать ботов в max и telegram',
            price = 100,
            user = self.user
        )
    
        self.client.login(username = 'Ivan',password='lollol212')
        self.url = reverse('shop:update_service',kwargs={'slug':self.service.slug})
        self.response = self.client.get(self.url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'update_service')
    
    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')
    
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class,views.ViewsUpdateService)

class ServiceDetailTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'

        )

    def setUp(self):
        self.service = Service.objects.create(
            title = 'Создание ботов',
            description = 'Я могу создавать ботов в max и telegram',
            price = 100,
            user = self.user
        )
    
        self.client.login(username = 'Ivan',password='lollol212')
        self.url = reverse('shop:detail_service',kwargs={'slug':self.service.slug})
        self.response = self.client.get(self.url)
    
    def test_url_asecc(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'detail_service')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')
    
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class,views.ViewsDetialService)
    
    #Model Task
class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'
        )
    
    def setUp(self):
        self.task = Task(
        title = 'Создание ботов',
            description = 'Я могу создавать ботов в max и telegram',
            price = 100,
            user = self.user)
    
    def test_create_task(self):
        self.assertIsInstance(self.task,Task)

    def test_title_Service(self):
        self.assertEqual(str(self.task),'Создание ботов')
    
    def test_saving_and_retrieving_task(self):
        first_task = Task()
        first_task.title = 'Первая задача'
        first_task.description = 'Описание первой задачи'
        first_task.price = 350
        first_task.user = self.user
        first_task.save()

        second_task = Task()
        second_task.title = 'second задача'
        second_task.description = 'Описание second задачи'
        second_task.price = 100
        second_task.user = self.user
        second_task.save()

        all_task = Task.objects.all()
        self.assertEqual(all_task.count(),2)
        
        first_saved_task = all_task[0]
        second_saved_task = all_task[1]

        self.assertEqual(first_saved_task.title,'Первая задача')
        self.assertEqual(first_saved_task.user, self.user)

        self.assertEqual(second_saved_task.title,'second задача')
        self.assertEqual(second_saved_task.user, self.user)


    # Для url связанные с Task Не заригистрирванный пользователь
class TaskPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/create_task/'
        client = Client()
        cls.response =client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code,302)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'create_task')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsFormTask)
    
class ListTaskPageGetTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/list_task/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'list_task')
    
    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')
    
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListTask)
    
class ListTaskMyPageGetTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/list_task_my/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_access(self):
        self.assertEqual(self.response.status_code,302)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'list_task_my')
    
    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')
    
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListTaskMy)



class UpdateTaskPageGetTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='Ivan',password='lollol212')
    

    def setUp(self):
        self.task = Task.objects.create(
            title = 'Создание ботов',
            description = 'Я могу создавать ботов в max и telegram',
            price = 100,
            user = self.user)
        self.client.login(username='Ivan',password='lollol212')
        self.url = reverse('shop:update_task',kwargs={'slug':self.task.slug})    

        self.response = self.client.get(self.url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)
    

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'update_task')
    
    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')
  
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class,views.ViewsUpdateTask)
class DetailTaskPageGetTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'

        )

    def setUp(self):
        self.task = Task.objects.create(
            title = 'Создание ботов',
            description = 'Я могу создавать ботов в max и telegram',
            price = 100,
            user = self.user
        )
    
        self.client.login(username = 'Ivan',password='lollol212')
        self.url = reverse('shop:detail_task',kwargs={'slug':self.task.slug})
        self.response = self.client.get(self.url)
    
    def test_url_asecc(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'detail_task')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace,'shop')
    
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class,views.ViewsDetailTask)