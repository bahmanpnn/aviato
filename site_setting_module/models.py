from django.db import models

class SiteSetting(models.Model):
    site_logo=models.ImageField(upload_to='images/site_logo/',blank=True,null=True)
    is_main_setting=models.BooleanField(default=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    phone=models.CharField(max_length=31,blank=True,null=True)
    fax=models.CharField(max_length=31,blank=True,null=True)
    email=models.EmailField(max_length=31,blank=True,null=True)
    copy_right=models.TextField(blank=True,null=True)
    about_us=models.TextField(blank=True,null=True)
    site_name=models.CharField(max_length=150)
    site_url=models.CharField(max_length=255)

    def __str__(self):
        return self.site_name


class FooterLinkItem(models.Model):
    title=models.CharField(max_length=150)
    url_title=models.URLField(max_length=200)


    def __str__(self):
        return self.title
    