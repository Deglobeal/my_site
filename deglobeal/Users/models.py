from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    second_name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="users_customuser_groups",  # Unique related_name
        related_query_name="users_customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="users_customuser_permissions",  # Unique related_name
        related_query_name="users_customuser",
    )

    def __str__(self):
        return self.username