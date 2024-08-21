from django.http import HttpRequest


def get_client_ip(request:HttpRequest):
    request=request.META
    
    if request.get('HTTP_X_FORWARDED_FOR'):
        ip=request.get('HTTP_X_FORWARDED_FOR').split(',')[0]

    else:
        ip=request.get('REMOTE_ADDR')

    return ip