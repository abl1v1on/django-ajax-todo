from django.urls import path

from . import views


app_name = 'app'


urlpatterns = [
    path('', views.index, name='home'),
    path('delete-note/', views.delete_note_view, name='delete_note'),
    path('create-note/', views.create_note, name='create_note'),
    path('complete-note/', views.complete_note_view, name='complete_note')
]
