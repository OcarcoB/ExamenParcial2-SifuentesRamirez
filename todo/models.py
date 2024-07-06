from django.db import models
from django.contrib.auth.models import User
from datetime import date  # Import date from datetime module

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(default=date.today)  # Provide a default value
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Provide a default value

    def __str__(self):
        return self.title
