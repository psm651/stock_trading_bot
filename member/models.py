from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=254, help_text='user email')
    password = models.TextField(help_text='encrypted text')
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    active = models.CharField(max_length=5, help_text='userId active status Y 사용중, H 휴면, N 삭제')
    tendency_id = models.IntegerField(help_text='stock tendency key')
    created = models.DateField(auto_now_add = True, help_text='created id date')
    updated = models.DateField(auto_now = True,help_text='update id date')
