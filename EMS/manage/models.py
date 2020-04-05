from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.IntegerField()
    pic = models.ImageField(upload_to='pics', null=True)

    class Meta:
        db_table = 'ems_employee'
