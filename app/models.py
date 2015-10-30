from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length = 30)
    date = models.DateField(auto_now = True)
    content = models.CharField(max_length = 140)
