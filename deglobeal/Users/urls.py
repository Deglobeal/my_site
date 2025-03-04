from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login page
    path('', views.home, name='home'),  # Home page
    path('sign_up/', views.sign_up, name='signup'),
    path('oauth/', include('social_django.urls', namespace='social')),
]