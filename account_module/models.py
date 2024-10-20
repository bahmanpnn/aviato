from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):

    phone_number=models.CharField(max_length=11,unique=True,null=True,blank=True)
    image=models.ImageField(upload_to='images/profiles',null=True,blank=True)
    email_active_code=models.CharField(max_length=100,null=True)
    about_user=models.TextField(null=True,blank=True)
    
    
    USERNAME_FIELD='phone_number' 
    # fields use for creating user in cli,default username_field(phone_number) is in and
    # doesn't need to add to fields again!

    REQUIRED_FIELDS=['email','username']
    
    objects = CustomUserManager()
    
    def __str__(self):
        
        if self.username:
            return self.username
        
        return self.email
    
    # def create_user(self, phone_number, email, username=None, password=None, **extra_fields):
    #     if not phone_number:
    #         raise ValueError('The Phone Number field must be set')
    #     if not email:
    #         raise ValueError('The Email field must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(phone_number=phone_number, email=email, username=username, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user


class UserAddressInformation(models.Model):
    address=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    receiver_full_name=models.CharField(max_length=255,blank=True,null=True) # can i use it in user model and set default self.user.get_full_name() ?
    country=models.CharField(max_length=255,default='Iran')
    phone=models.CharField(max_length=15)