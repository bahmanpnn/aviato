from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Slider(models.Model):
    title=models.CharField(max_length=100)
    # text=RichTextField(config_name='default')  # Specify the config if needed
    text=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    image=models.ImageField(upload_to='sliders/',null=True)
    link_url=models.URLField(null=True,blank=True)
    btn_text=models.CharField(max_length=100,null=True,blank=True)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    

class UserEmailSubscribe(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email
