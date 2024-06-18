import datetime
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
class Meeting(models.Model):
    meeting_code=models.CharField(max_length=100)
    meeting_dt=models.DateField(default=datetime.datetime.now())
    meeting_subject=models.CharField(max_length=100)
    meeting_np=models.IntegerField()