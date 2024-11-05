from django.shortcuts import redirect
from django.urls import reverse


def is_admin_permission_checker_factory(data='data'):
    def is_admin_permission_checker(func):
        def wrapper(request,*args, **kwargs):
            print(data)
            if request.user.is_authenticated and request.user.is_staff:
                return func(request,*args, **kwargs)
            else:
                return redirect(reverse('login-page'))
        return wrapper
    return is_admin_permission_checker


def is_admin_permission_checker(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return func(request,*args, **kwargs)
        else:
            return redirect(reverse('login-page'))
    return wrapper


def is_superuser_permission_checker(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return func(request,*args, **kwargs)
        else:
            return redirect(reverse('login-page'))
    return wrapper


def is_authenticated_permission(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated:
            return func(request,*args, **kwargs)
        else:
            return redirect(reverse('login-page'))
    return wrapper