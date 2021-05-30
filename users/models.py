from django.db import models

# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=20)

    def __str__(self):
        return self.user_type

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    area_code = models.CharField(max_length=6)
    mobile= models.IntegerField()
    user_type= models.ForeignKey(UserType,on_delete=models.CASCADE)
    