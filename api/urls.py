from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views


app_name = 'api_v1'


urlpatterns = [
    path('token/', views.MyTokenView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.SignUpUserView.as_view(), name='signup_user'),
    path('notes/', views.UserNotesListView.as_view(), name='user_notes_list'),
    path('notes/<int:pk>/', views.UserNoteRetriveView.as_view(), name='user_note'),
]
