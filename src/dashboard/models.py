from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoCatagory(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=200)

    def __str__(self):
        return self.header

class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ForeignKey(TodoCatagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
