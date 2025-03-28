import pytest


@pytest.fixture
def user(django_user_model):
<<<<<<< HEAD
    return django_user_model.objects.create_user(username='TestUser', password='1234567')
=======
    return django_user_model.objects.create_user(
        username='TestUser', password='1234567'
    )
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c


@pytest.fixture
def user_2(django_user_model):
<<<<<<< HEAD
    return django_user_model.objects.create_user(username='TestUser2', password='1234567')
=======
    return django_user_model.objects.create_user(
        username='TestUser2', password='1234567'
    )
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c


@pytest.fixture
def another_user(django_user_model):
<<<<<<< HEAD
    return django_user_model.objects.create_user(username='TestUserAnother', password='1234567')
=======
    return django_user_model.objects.create_user(
        username='TestUserAnother', password='1234567'
    )
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c


@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    return client
