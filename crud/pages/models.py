from django.db import models

# Create your models here.


class Crud(models.Model):
    name = models.CharField(max_length=127,null=True,blank=True)
    adress = models.CharField(max_length=127,null=True,blank=True)
    email = models.EmailField(max_length=127,null=True,blank=True)
    phone = models.CharField(max_length=127,null=True,blank=True)
    

    def __str__(self):
        return self.name



