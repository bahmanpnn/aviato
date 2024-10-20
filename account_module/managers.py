from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email, username=None, password=None, **extra_fields):
        # if not phone_number:
        #     raise ValueError('The Phone Number field must be set')
        # if not email:
        #     raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, email, username, password, **extra_fields)
