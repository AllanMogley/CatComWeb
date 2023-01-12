from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=27)
    phone = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(15)])
    residence = models.CharField(max_length=10)
    studyyear = models.IntegerField()
