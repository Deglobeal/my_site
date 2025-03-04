from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Title of the task"
    )
    description = models.TextField(
        blank=True,
        help_text="Detailed description of the task"
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        help_text="Automatically records creation date/time"
    )
    done = models.BooleanField(
        default=False,
        help_text="Checkbox for task completion"
    )
    done_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Records date/time when task was marked done"
    )
    canceled = models.BooleanField(
        default=False,
        help_text="Marks if task was canceled"
    )
    canceled_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Records date/time when task was canceled"
    )

    def save(self, *args, **kwargs):
        """Automatically set dates when done/canceled status changes"""
        # Update done_date only when marking as done
        if self.done and not self.done_date:
            self.done_date = timezone.now()
        elif not self.done:
            self.done_date = None
            
        # Update canceled_date only when marking as canceled
        if self.canceled and not self.canceled_date:
            self.canceled_date = timezone.now()
        elif not self.canceled:
            self.canceled_date = None
            
        super().save(*args, **kwargs)

    def __str__(self):
        status = "Done" if self.done else "Pending"
        return f"{self.title} ({status})"