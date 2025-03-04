from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todos import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)  # Creates CRUD endpoints at /api/todos/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]