#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py shell -c "
from django.contrib.auth import get_user_model, authenticate
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    user, created = User.objects.get_or_create(username=username)

    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()

    print('Superuser username:', user.username)
    print('Is staff:', user.is_staff)
    print('Is superuser:', user.is_superuser)
    print('Is active:', user.is_active)

    test_user = authenticate(username=username, password=password)

    if test_user:
        print('PASSWORD CHECK: SUCCESS')
    else:
        print('PASSWORD CHECK: FAILED')
else:
    print('Superuser credentials are missing.')
"