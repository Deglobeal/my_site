from django.contrib import admin
from .models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'done', 'done_date', 'canceled', 'canceled_date')
    list_filter = ('done', 'canceled')
    search_fields = ('title', 'description')
    
