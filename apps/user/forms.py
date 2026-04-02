from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class FormRegisterUser(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(max_length=50,widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput())
    avatar = forms.ImageField(required=False)
    

    class Meta:
        model = User
        fields = ('username','email','password1','password2','avatar')


class FormLoginUser(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False)
