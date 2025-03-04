from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('news/', views.news, name='news'),
    path('updates/', views.updates, name='updates'),
    path('cv_page/', views.cv_page, name='cv_page'),
    path('certificate/', views.certificate, name='certificate'),
    path('about/', views.about, name='about'),
    path('social/', views.social, name='social'),
    path('email/', views.email, name='email'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('User/', include('Users.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]