from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
    path('user/', include('users.urls', namespace='user')),
    path('api/v1/', include('api.urls', namespace='api_v1'))
]
