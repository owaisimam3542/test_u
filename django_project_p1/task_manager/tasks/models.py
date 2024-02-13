from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Todo', 'Todo'), ('Inprogress', 'In Progress'), ('Done', 'Done')])
    created_at = models.DateTimeField(auto_now_add=True)

class TaskMember(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
#from django.db import models

# Create your models here.
