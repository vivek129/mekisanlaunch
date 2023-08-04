# Create your models here.
from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    endtime = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    
class emails(models.Model):
    email= models.EmailField()

    def __str__(self):
        return self.email