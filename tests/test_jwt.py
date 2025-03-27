<<<<<<< HEAD
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


=======
from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
class TestJWT:
    url_create = '/api/v1/jwt/create/'
    url_refresh = '/api/v1/jwt/refresh/'
    url_verify = '/api/v1/jwt/verify/'

<<<<<<< HEAD
    @pytest.mark.django_db(transaction=True)
    def test_jwt_create__invalid_request_data(self, client, user):
        url = self.url_create
        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        fields_invalid = ['username', 'password']
        for field in fields_invalid:
            assert field in response.json().keys(), (
                f'Убедитесь, что при запросе `{url}` без параметров, '
                f'возвращается код {code_expected} с сообщением о том, '
                'при обработке каких полей возникла ошибка.'
                f'Не найдено поле {field}'
            )

        username_invalid = 'invalid_username_not_exists'
        password_invalid = 'invalid pwd'
        data_invalid = {
            'username': username_invalid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = 'detail'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с некорректным username, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )
        username_valid = user.username
        data_invalid = {
            'username': username_valid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = 'detail'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с некорректным password, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )

    @pytest.mark.django_db(transaction=True)
=======
    def check_request_with_invalid_data(self, client, url, invalid_data,
                                        expected_fields):
        response = client.post(url)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            f'Если POST-запрос, отправленный к `{url}`, не содержит всех '
            'необходимых данных - должен вернуться ответ со статусом 400.'
        )

        response = client.post(url, data=invalid_data)
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Убедитесь, что POST-запрос с некорректными данными, '
            f'отправленный к `{url}`, возвращает ответ со статусом 401.'
        )
        for field in expected_fields:
            assert field in response.json(), (
                'Убедитесь, что в ответе на POST-запрос с некорректными '
                f'данными, отправленный к `{url}`, содержится поле `{field}` '
                'с соответствующим сообщением.'
            )

    def test_jwt_create__invalid_request_data(self, client, user):
        url = self.url_create
        response = client.post(url)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Убедитесь, что POST-запрос без необходимых данных, отправленный '
            f'к `{url}`, возвращает ответ со статусом код 400.'
        )
        fields_invalid = ['username', 'password']
        for field in fields_invalid:
            assert field in response.json(), (
                'Убедитесь, что в ответе на POST-запрос без необходимых '
                'данных, отправленный к `{url}` содержится информация об '
                'обязательных для этого эндпоинта полях. Сейчас ответ не '
                f'содержит информацию о поле `{field}`.'
            )

        invalid_data = (
            {
                'username': 'invalid_username_not_exists',
                'password': 'invalid pwd'
            },
            {
                'username': user.username,
                'password': 'invalid pwd'
            }
        )
        field = 'detail'
        for data in invalid_data:
            response = client.post(url, data=data)
            assert response.status_code == HTTPStatus.UNAUTHORIZED, (
                'Убедитесь, что POST-запрос с некорректными данными, '
                f'отправленный к`{url}`, возвращает ответ со статусом 401.'
            )
            assert field in response.json(), (
                'Убедитесь, что в ответе на POST-запрос с некорректными '
                f'данными, отправленный к `{url}`, содержится поле `{field}` '
                'с сообщением об ошибке.'
            )

>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
    def test_jwt_create__valid_request_data(self, client, user):
        url = self.url_create
        valid_data = {
            'username': user.username,
            'password': '1234567'
        }
        response = client.post(url, data=valid_data)
<<<<<<< HEAD
        code_expected = 200
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидными данными, '
            f'возвращается код {code_expected}'
        )
        fields_in_response = ['refresh', 'access']
        for field in fields_in_response:
            assert field in response.json().keys(), (
                f'Убедитесь, что при запросе `{url}` с валидными данными, '
                f' в ответе возвращается код {code_expected} с ключами '
                f'{fields_in_response}, где содержатся токены'
            )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_refresh__invalid_request_data(self, client):
        url = self.url_refresh

        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        data_invalid = {
            'refresh': 'invalid token'
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с невалидным значением параметра refresh, '
            f'возвращается код {code_expected}'
        )
        fields_expected = ['detail', 'code']
        for field in fields_expected:
            assert field in response.json(), (
                f'Убедитесь, что при запросе `{url}` с невалидным значением параметра refresh, '
                f'возвращается код {code_expected} с соответствующим сообщением '
                f'в поле {field}'
            )

    @pytest.mark.django_db(transaction=True)
=======
        assert response.status_code == HTTPStatus.OK, (
            'Убедитесь, что POST-запрос с корректными данными, отправленный '
            f'к `{url}`, возвращает ответ со статусом 200.'
        )
        fields_in_response = ['refresh', 'access']
        for field in fields_in_response:
            assert field in response.json(), (
                'Убедитесь, что в ответе на  POST-запрос с корректными '
                f'данными, отправленный к `{url}`, содержится поле `{field}` '
                'с соответствующим токеном.'
            )

    def test_jwt_refresh__invalid_request_data(self, client):
        invalid_data = {
            'refresh': 'invalid token'
        }
        fields_expected = ['detail', 'code']
        self.check_request_with_invalid_data(
            client, self.url_refresh, invalid_data, fields_expected
        )

>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
    def test_jwt_refresh__valid_request_data(self, client, user):
        url = self.url_refresh
        valid_data = {
            'username': user.username,
            'password': '1234567'
        }
        response = client.post(self.url_create, data=valid_data)
        token_refresh = response.json().get('refresh')
<<<<<<< HEAD
        code_expected = 200
        response = client.post(url, data={'refresh': token_refresh})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром refresh, '
            f'возвращается код {code_expected}'
        )
        field = 'access'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с валидным параметром refresh, '
            f'возвращается код {code_expected} и параметр access, в котором передан новый токен'
        )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_verify__invalid_request_data(self, client):
        url = self.url_verify

        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        data_invalid = {
            'token': 'invalid token'
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с невалидным значением параметра token, '
            f'возвращается код {code_expected}'
        )
        fields_expected = ['detail', 'code']
        for field in fields_expected:
            assert field in response.json(), (
                f'Убедитесь, что при запросе `{url}` с невалидным значением параметра token, '
                f'возвращается код {code_expected} с соответствующим сообщением '
                f'в поле {field}'
            )

    @pytest.mark.django_db(transaction=True)
=======
        response = client.post(url, data={'refresh': token_refresh})
        assert response.status_code == HTTPStatus.OK, (
            'Убедитесь, что POST-запрос с корректными данными, отправленный '
            f'к `{url}`, возвращает ответ со статусом 200.'
        )
        field = 'access'
        assert field in response.json(), (
            'Убедитесь, что в ответе на POST-запрос с корректными данными, '
            f'отправленный к `{url}`, содержится поле `{field}`, '
            'содержащее новый токен.'
        )

    def test_jwt_verify__invalid_request_data(self, client):
        invalid_data = {
            'token': 'invalid token'
        }
        fields_expected = ['detail', 'code']
        self.check_request_with_invalid_data(
            client, self.url_verify, invalid_data, fields_expected
        )

>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
    def test_jwt_verify__valid_request_data(self, client, user):
        url = self.url_verify
        valid_data = {
            'username': user.username,
            'password': '1234567'
        }
        response = client.post(self.url_create, data=valid_data)
<<<<<<< HEAD
        token_access = response.json().get('access')
        token_refresh = response.json().get('refresh')
        code_expected = 200
        response = client.post(url, data={'token': token_access})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром token, '
            f'возвращается код {code_expected}. '
            'Валидацию должны проходить как refresh, так и access токены'
        )
        response = client.post(url, data={'token': token_refresh})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром token, '
            f'возвращается код {code_expected}. '
            'Валидацию должны проходить как refresh, так и access токены'
        )
=======
        response_data = response.json()

        for token in (response_data.get('access'),
                      response_data.get('refresh')):
            response = client.post(url, data={'token': token})
            assert response.status_code == HTTPStatus.OK, (
                'Убедитесь, что POST-запрос с корректными данными, '
                f'отправленный к `{url}`, возвращает ответ со статусом 200. '
                'Корректными данными считаются `refresh`- и `access`-токены.'
            )
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
