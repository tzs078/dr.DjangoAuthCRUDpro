from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    pass 

class DocModel(models.Model):
    GENDER_TYPES={
        ('Male','Male'),
        ('Female','Female'),
    }
    Name = models.CharField(max_length=200,null=True)
    Email = models.EmailField(null=True)
    Phone = models.PositiveIntegerField(null=True)
    Address = models.CharField(max_length=100,null=True)
    Gender = models.CharField(choices=GENDER_TYPES,max_length=50,null=True)
    Image = models.ImageField(upload_to='Media/DocImage',null=True)

    def __str__(self):
        return f'{self.name}'



