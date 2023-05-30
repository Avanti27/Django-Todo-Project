from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.(create table)

def check_cduration(value):

    if value<=0:

        raise ValidationError('Course duration cannot be zero')


def check_price(value):

    if value<=0:
        
        raise ValidationError('Course price cannot be zero')

class CourseManager(models.Manager):

    def sort_desc_price(x):
        #return x.order_by('-cprice').filter(cdur__gt=40) 
        return super().order_by('-cprice').filter(cdur__gt=20) 

class Student(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField()


class Course(models.Model):

    cname=models.CharField(max_length=50,unique=True)
    #cdur=models.IntegerField(primarykey=True)
    cdur=models.IntegerField(validators=[check_cduration])
    cprice=models.FloatField(validators=[check_price])
    #c_manager=models.Manager()#overriding default which is object
    objects=models.Manager()
    c_manager=CourseManager()

'''
    def __str__(self):

        return self.cname

'''


    