from django.db import models

# Create your models here.
from django.db import models
 
class posts(models.Model):
    author = models.CharField(max_length = 30)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    likes = models.IntegerField(default=0)
