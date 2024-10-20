from .models import User

def create_user(strategy, details, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    email = details.get('email')
    username = details.get('username') or details.get('email').split('@')[0]
    phone_number = details.get('phone_number', '')  # Handle phone_number gracefully

    # Ensure username uniqueness
    base_username = username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1

    if email:
        user = User.objects.create_user(
            phone_number=phone_number,
            email=email,
            username=username
        )
        return {'is_new': True, 'user': user}
    else:
        raise ValueError("Email must be set")

    return {'is_new': False}
