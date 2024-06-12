from pyexpat import model
from django.db import models

# Create your models here.
class Department(models.Model):
    name =models.CharField(max_length=100, null=False)
    location =models.CharField(max_length=100)

    class Role(models.Model):
        name =models.CharField(max_length=100, null=False)

def __str__(self):
    return self.name

#Employee Database Models
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(max_length=1000000000000)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)
    