from django.db import models


class ContactUs(models.Model):
    full_name=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    created_date=models.DateTimeField(auto_now_add=True)
    is_read_by_admin=models.BooleanField(default=False)
    admin_response=models.TextField()

    def __str__(self):
        return f'{self.email} - {self.subject}'
    
    class Meta:
        verbose_name='contact us'
        verbose_name_plural='contact us'
    
