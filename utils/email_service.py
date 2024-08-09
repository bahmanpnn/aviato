from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def email_service(subject,to,context,template_name):
    
    try:
        html_message=render_to_string(template_name,context)
        plain_message=strip_tags(html_message)
        
        from_website_email=settings.EMAIL_HOST_USER
        send_mail(subject,plain_message,from_website_email,[to],html_message=html_message)
        print('email sent!!')
    
    except:
            print('error')