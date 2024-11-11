from django.db import models
from ckeditor.fields import RichTextField


class SiteSetting(models.Model):
    site_logo=models.ImageField(upload_to='images/site_logo/',blank=True,null=True)
    is_main_setting=models.BooleanField(default=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    phone=models.CharField(max_length=31,blank=True,null=True)
    fax=models.CharField(max_length=31,blank=True,null=True)
    email=models.EmailField(max_length=31,blank=True,null=True)
    copy_right=models.TextField(blank=True,null=True)
    # about_us=models.TextField(blank=True,null=True)
    about_us=RichTextField(blank=True,null=True)
    site_name=models.CharField(max_length=150)
    site_url=models.CharField(max_length=255)
    
    #social media
    facebook=models.URLField(blank=True,null=True)
    instagram=models.URLField(blank=True,null=True)
    telegram=models.URLField(blank=True,null=True)
    twitter=models.URLField(blank=True,null=True)
    pinterest=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.site_name


class FooterLinkItem(models.Model):
    title=models.CharField(max_length=150)
    url_title=models.URLField(max_length=200)


    def __str__(self):
        return self.title


class TeamMember(models.Model):
    image=models.ImageField(upload_to='images/team_members',blank=True,null=True)
    full_name=models.CharField(max_length=127)
    position=models.CharField(max_length=127)


class Award(models.Model):
    image=models.ImageField(upload_to='images/awards',null=True)

