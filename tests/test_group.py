<<<<<<< HEAD
=======
from http import HTTPStatus

>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
import pytest

from posts.models import Group


<<<<<<< HEAD
class TestGroupAPI:

    @pytest.mark.django_db(transaction=True)
    def test_group_not_found(self, client, post, group_1):
        response = client.get('/api/v1/groups/')

        assert response.status_code != 404, (
            'Страница `/api/v1/groups/` не найдена, проверьте этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_group_list_not_auth(self, client, post, group_1):
        response = client.get('/api/v1/groups/')
        assert response.status_code == 200, (
            'Проверьте, что `/api/v1/groups/` при запросе без токена возвращаете статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_group_single_not_auth(self, client, group_1):
        response = client.get(f'/api/v1/groups/{group_1.id}/')
        assert response.status_code == 200, (
            'Проверьте, что `/api/v1/groups/{group.id}/` при запросе без токена возвращаете статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_group_get(self, user_client, post, another_post, group_1, group_2):
        response = user_client.get('/api/v1/groups/')
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/groups/` с токеном авторизации возвращается статус 200'
        )

        test_data = response.json()

        assert type(test_data) == list, (
            'Проверьте, что при GET запросе на `/api/v1/groups/` возвращается список'
        )

        assert len(test_data) == Group.objects.count(), (
            'Проверьте, что при GET запросе на `/api/v1/groups/` возвращается весь список групп'
        )

        groups_cnt = Group.objects.count()
        test_group = test_data[0]

        assert 'title' in test_group, (
            'Проверьте, что добавили `title` в список полей `fields` сериализатора модели Group'
        )

        assert len(test_data) == groups_cnt, (
            'Проверьте, что при GET запросе на `/api/v1/groups/` возвращается весь список групп'
        )

    @pytest.mark.django_db(transaction=True)
    def test_group_cannot_create(self, user_client, group_1, group_2):
        group_count = Group.objects.count()

        data = {}
        response = user_client.post('/api/v1/groups/', data=data)
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе на `/api/v1/groups/` нельзя создать сообщество через API'
        )

        data = {'title': 'Группа  номер 3'}
        response = user_client.post('/api/v1/groups/', data=data)
        assert response.status_code == 405, (
            'Проверьте, что при POST запросе на `/api/v1/groups/` нельзя создать сообщество через API'
        )

        assert group_count == Group.objects.count(), (
            'Проверьте, что при POST запросе на `/api/v1/groups/` нельзя создать сообщество через API'
        )

    @pytest.mark.django_db(transaction=True)
    def test_group_get(self, user_client, post, post_2, another_post, group_1, group_2):
        response = user_client.get('/api/v1/groups/')
        assert response.status_code == 200, (
            'Страница `/api/v1/groups/` не найдена, проверьте этот адрес в *urls.py*'
        )
        test_data = response.json()
        groups_cnt = Group.objects.all().count()
        assert len(test_data) == groups_cnt, (
            'Проверьте, что при GET запросе на `/api/v1/groups/` возвращается список всех сообществ'
        )

        response = user_client.get(f'/api/v1/groups/{group_2.id}/')
        assert isinstance(response.json(), dict), (
            'При запросе `/api/v1/groups/{id}/` должен возвращаться словарь'
        )

        g = Group.objects.filter(id=group_2.id)
        json_response = response.json()
        for k in json_response:
            assert k in g.values()[0] and json_response[k] == g.values()[0][k], (
                'Проверьте, что при GET запросе на `/api/v1/groups/{id}/` '
                'возвращается информация о соответствующем сообществе'
            )

        response = user_client.get(f'/api/v1/groups/{group_1.id}/')
        assert isinstance(response.json(), dict), (
            'При запросе `/api/v1/groups/{id}/` должен возвращаться словарь'
        )
        g = Group.objects.filter(id=group_1.id)
        json_response = response.json()
        for k in json_response:
            assert k in g.values()[0] and json_response[k] == g.values()[0][k], (
                'Проверьте, что при GET запросе на `/api/v1/groups/{id}/` '
                'возвращается информация о соответствующем сообществе'
            )
=======
@pytest.mark.django_db(transaction=True)
class TestGroupAPI:

    group_url = '/api/v1/groups/'
    group_detail_url = '/api/v1/groups/{group_id}/'

    def check_group_info(self, group_info, url):
        assert 'id' in group_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию о '
            'группе. Проверьте, что поле `id` добавлено в список полей '
            '`fields` сериализатора модели `Group`.'
        )
        assert 'title' in group_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию о '
            'группе. Проверьте, что поле `title` добавлено в список полей '
            '`fields` сериализатора модели `Group`.'
        )
        assert 'slug' in group_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию о '
            'группе. Проверьте, что поле `slug` добавлено в список полей '
            '`fields` сериализатора модели `Group`.'
        )
        assert 'description' in group_info, (
            f'Ответ на GET-запрос к `{url}` содержит неполную информацию о '
            'группе. Проверьте, что поле `description` добавлено в список '
            'полей `fields` сериализатора модели `Group`.'
        )

    def test_group_not_found(self, client, group_1):
        response = client.get(self.group_url)

        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.group_url}` не найден, проверьте настройки в '
            '*urls.py*.'
        )

    def test_group_list_not_auth(self, client, post, group_1):
        response = client.get(self.group_url)
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            f'`{self.group_url}` возвращает ответ со статусом 200.'
        )

    def test_group_page_not_found(self, client, group_1):
        response = client.get(
            self.group_detail_url.format(group_id=group_1.id)
        )
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.group_detail_url}` не найден, проверьте '
            'настройки в *urls.py*.'
        )

    def test_group_single_not_auth(self, client, group_1):
        response = client.get(
            self.group_detail_url.format(group_id=group_1.id)
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            f'`{self.group_detail_url}` возвращает ответ со статусом 200.'
        )

    def test_group_auth_get(self, user_client, group_1, group_2):
        response = user_client.get(self.group_url)
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что для авторизованного пользователя GET-запрос к '
            f'{self.group_url}` возвращает ответ со статусом 200.'
        )

        test_data = response.json()
        assert isinstance(test_data, list), (
            'Проверьте, что для авторизованного пользователя '
            f'GET-запрос к `{self.group_url}` возвращает информацию о группах '
            'в виде списка.'
        )
        assert len(test_data) == Group.objects.count(), (
            'Проверьте, что для авторизованного пользователя GET-запрос к '
            f'`{self.group_url}` возвращает информацию обо всех существующих '
            'группах.'
        )

        test_group = test_data[0]
        self.check_group_info(test_group, self.group_url)

    def test_group_create(self, user_client, group_1, group_2):
        data = {'title': 'Группа  номер 3'}
        response = user_client.post(self.group_url, data=data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            'Убедитесь, что группу можно создавать только через админку и что '
            f'при попытке создать её через POST-запрос к `{self.group_url}` '
            'возвращается статус 405.'
        )

    def test_group_page_auth_get(self, user_client, group_1):
        response = user_client.get(
            self.group_detail_url.format(group_id=group_1.id)
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что при GET-запросе авторизованного пользователя к '
            f'`{self.group_detail_url}` возвращается ответ со статусом 200.'
        )

        test_data = response.json()
        assert isinstance(test_data, dict), (
            'Проверьте, что при GET-запросе авторизованного пользователя к '
            f'`{self.group_detail_url}` информация о группе возвращается в '
            'виде словаря.'
        )
        self.check_group_info(test_data, '/api/v1/groups/{group_id}/')
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
