from django.test import TestCase,SimpleTestCase,Client
from appss.user.tests import Usertest
from . import views
#для не авторизованного пользователя

class ChatPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/chat/list_task/chat/'
        client = Client()
        cls.response = client.get(url)
    def test_url_access(self):
        self.assertEqual(self.response.status_code, 302)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'list_task_chat')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListChatTask)



class ServiceChatPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/chat/list_service/chat/'
        client = Client()
        cls.response = client.get(url)
    def test_url_access(self):
        self.assertEqual(self.response.status_code, 302)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'list_service_chat')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListChatService)

#для авторизованного пользователя
class ChatUserPageGetTests(Usertest):
    def setUp(self) -> None:
        self.client.login(username='Ivan', password='lollol212')
        self.url = '/chat/list_task/chat/'
        self.response = self.client.get(self.url)
    
    def test_url_access(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'list_task_chat')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListChatTask)    
    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'chat/task/list_chat.html')

class UserServiceChatPageGetTests(Usertest):
    def setUp(self) -> None:
        self.client = Client()
        self.client.login(username='Ivan', password='lollol212')
        url = '/chat/list_service/chat/'
        self.response = self.client.get(url)
    def test_url_access(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'list_service_chat')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsListChatService)
    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'chat/task/list_chat.html')
