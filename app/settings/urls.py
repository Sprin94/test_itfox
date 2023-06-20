from django.contrib import admin
from rest_framework.authtoken import views as token_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls', namespace='news')),
    path('auth/', token_views.obtain_auth_token),
]
