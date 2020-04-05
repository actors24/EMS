from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    realname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)

    class Meta:
        db_table = 'ems_user'
