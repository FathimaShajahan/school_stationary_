
# Create your models here.
# models.py
from django.db import models



class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials_provide = models.ManyToManyField(Material)
    
    def __str__(self) :
        return self.name
