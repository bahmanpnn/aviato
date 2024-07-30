from django.db import models
from django.urls import reverse


class Slider(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    # image=models.ImageField(upload_to='sliders/')

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    