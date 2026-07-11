from django.test import TestCase,SimpleTestCase
from django.test import Client
from . import views
from .models import User
#url test
class RegisterPageGetTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_access(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name,'register')
    
    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsRegisterUser)

    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'user/register.html')


# Не заригестрирванный пользователь 
class LoginPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/login/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'login')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsLoginUser)

class LogoutPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/logout/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,302)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'logout')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsLogout)
        # Это нужно проверить на зарегистрирванном пользователе 
    '''def test_template_name(self):
        self.assertTemplateUsed(self.response, 'user/logout.html')'''

class DetailUserMyPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/profile/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,302)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'detail_user_my')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsDetailProfileMy)

class UpdateProfilePageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/profile/update/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,302)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'update_profile')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsUpdateProfile)
    
class MenuGuestPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/menu_guest/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'menu_guest')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.GuestMenuView)

    def test_template_name(self):
        self.assertTemplateUsed(self.response,"templates_htmx/menu_not_in.html")

class MenuUserPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        url = '/user/menu_user/'
        client = Client()
        cls.response = client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,302)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'menu_user')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsGetMenu)



# Заригестрирванный пользователь 
class Usertest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create_user(
            username = 'Ivan',
            password='lollol212'
        )
    
class UserLogoutPageGetTests(Usertest):
    def setUp(self):
        self.client.login(username='Ivan', password='lollol212')
        self.url = '/user/logout/'
        self.response = self.client.get(self.url)

    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'logout')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsLogout)
       
    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'user/logout.html')

class UserDetailUserMyPageGetTests(Usertest):
   
    def setUp(self):
        self.client.login(username='Ivan', password='lollol212')
        self.url = '/user/profile/'
        self.response = self.client.get(self.url)
   
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'detail_user_my')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
        
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsDetailProfileMy)

    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'user/detail_myuser.html')
        
class UserUpdateProfilePageGetTests(Usertest):
    def setUp(self) -> None:
        self.url = '/user/profile/update/'
        self.client.login(username='Ivan', password='lollol212')
        self.response = self.client.get(self.url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'update_profile')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsUpdateProfile)
    
    def test_template_name(self):
        self.assertTemplateUsed(self.response,"user/update_profale.html")

class UserMenuGuestPageGetTests(Usertest):
    def setUp(self) -> None:
        url = '/user/menu_guest/'
        self.client.login(username='Ivan', password='lollol212')
        self.response = self.client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,302)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'menu_guest')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.GuestMenuView)

    def test_template_name(self):
        self.assertTemplateNotUsed(self.response,"templates_htmx/menu_not_in.html")

class UserMenuUserPageGetTests(Usertest):
    def setUp(self) -> None:
        url = '/user/menu_user/'
        self.client.login(username='Ivan', password='lollol212')
        self.response = self.client.get(url)
    
    def test_url_aceess(self):
        self.assertEqual(self.response.status_code,200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'menu_user')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, '') 
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, views.ViewsGetMenu)
    def test_template_name_buyer(self):
        self.assertTemplateUsed(self.response,"templates_htmx/menu_user_buyer.html")
        
    def test_template_name_seller(self):
        self.user.profile.status = True
        self.user.profile.save()
        url = '/user/menu_user/'
        response = self.client.get(url)
        self.assertTemplateUsed(response,"templates_htmx/menu_user_seller.html")
        
