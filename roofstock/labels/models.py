from django.db import models

# Create your models here.

class Label(models.Model):
    fromCompany = models.CharField(max_length=46,null=True)
    fromStreet1 = models.CharField(max_length=46, null=True)
    fromStreet2 = models.CharField(max_length=46, null=True)
    fromCity = models.CharField(max_length=46, null=True)
    fromState = models.CharField(max_length=46, null=True)
    fromZip = models.IntegerField(null=True)
    fromPhone = models.IntegerField(null=True)

    toName = models.CharField(max_length=46, null=True)
    toCompany = models.CharField(max_length=46,null=True)
    toStreet1 = models.CharField(max_length=46, null=True)
    toCity = models.CharField(max_length=46, null=True)
    toState = models.CharField(max_length=46, null=True)
    toZip = models.IntegerField(null=True)