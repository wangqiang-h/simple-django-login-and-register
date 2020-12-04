from django.db import models
from django.utils import timezone

# Create your models here.
"""
parent 和 student 是一对一的关系
teacher class 是多对多的关系
class 和student 是1对多的关系
"""


class Student(models.Model):
    name = models.CharField(max_length=4)
    age = models.IntegerField(default=20)
    birthday = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
