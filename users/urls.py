from django.urls import path

from . import views


app_name = 'user'


urlpatterns = [
    path('sign-in/', views.LoginUserView.as_view(), name='signin'),
    path('sign-up/', views.CreateUserView.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout')
]
