from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import RegisterUserForm, LoginUserForm


class CreateUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('user:signin')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('app:home')


def logout_user(request):
    logout(request)
    return redirect('user:signin')
