from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone_number=models.CharField(max_length=11,unique=True,null=True)
    image=models.ImageField(upload_to='images/profiles',null=True,blank=True)
    
    
    USERNAME_FIELD='phone_number' 
    # fields use for creating user in cli,default username_field(phone_number) is in and
    # doesn't need to add to fields again!

    REQUIRED_FIELDS=['email','username']