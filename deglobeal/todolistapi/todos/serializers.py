from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id', 
            'title', 
            'description', 
            'date_added', 
            'done', 
            'done_date', 
            'canceled', 
            'canceled_date'
        ]
        read_only_fields = ['date_added', 'done_date', 'canceled_date']  # Auto-set fields