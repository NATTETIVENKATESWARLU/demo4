from django.db import models
from django.contrib.auth.models import User

# Task Model
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# User Model is already provided by Django, no need to create it manually unless customization is needed.
