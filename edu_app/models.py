from django.db import models

# Create your models here.

class News(models.Model):
    heading = models.CharField(max_length=150)
    news_text = models.TextField()
    date = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')

class UpcomingEvent(models.Model):
    address = models.CharField(max_length=60)
    heading = models.CharField(max_length=150)
    date = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')