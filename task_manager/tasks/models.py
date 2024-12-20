from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import now

class Task(models.Model):
  PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
  STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
  
  title = models.CharField(max_length=100)
  description = models.TextField()
  priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
  status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
  due_date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')


  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['-due_date']
    

