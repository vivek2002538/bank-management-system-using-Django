from django.db import models

# Create your models here.
class gender(models.Model):
    name=models.CharField(max_length=6)
    def __str__(self):
        return self.name

class account(models.Model):
    acc_num=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    dob=models.DateField()
    aadhar=models.PositiveBigIntegerField(unique=True)
    pan=models.CharField(max_length=10,unique=True)
    phone=models.PositiveBigIntegerField(unique=10)
    gender=models.ForeignKey(gender,on_delete=models.CASCADE)
    pin=models.CharField(max_length=64)
    bal=models.IntegerField(default=1000)
