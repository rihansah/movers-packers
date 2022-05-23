from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE())
    mobile = models.CharField(max_length=15,null=True)
    location = models.CharField(max_length=200,null=True)
    shiftingloc = models.CharField(max_length=200,null=True)
    briefitems = models.CharField(max_length=100,null=True)
    items = models.CharField(max_length=5000,null=True)
    professional = models.CharField(max_length=200,null=True)
    requestdate = models.DateField(null=True)
    remark = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=30, null= True)
    updationdate = models.DateField(null=True)