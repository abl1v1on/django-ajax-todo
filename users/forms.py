from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите логин'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите почту'
    }))

    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Повторите пароль'
    }))
    

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data['email']

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже существует')
        return email


class LoginUserForm(AuthenticationForm):
    # AuthenticationForm аутентифицирует по username, но USERNAME_FIELD стоит email, поэтому поле здесь именно username
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите почту',
        'id': 'email'
    }))

    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите пароль',
        'id': 'password'
    }))
