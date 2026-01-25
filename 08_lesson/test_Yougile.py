import requests
import pytest

base_url = "https://ru.yougile.com/api-v2"
api_key = ""
my_headers = {
    "Authorization": f'Bearer {api_key}',
    "Content-Type": "application/json"
}


def get_projects_list():
    response = requests.get(base_url+'/projects', headers=my_headers)
    assert response.status_code == 200
    return response.json()


def create_projects(title):
    project = {
            "title": title,
     }

    response = requests.post(base_url + '/projects', json=project, headers=my_headers)
    assert response.status_code == 201
    return response.json()


def get_projects(id):
    response = requests.get(base_url + '/projects/' + str(id), headers=my_headers)
    assert response.status_code == 200
    return response.json()


def edit(new_id, new_title):
    project = {
        "title": new_title,
    }
    response = requests.put(base_url + '/projects/' + str(new_id), json=project, headers=my_headers)
    assert response.status_code == 200

    return response.json()


# ============ПОЗИТИВНЫЕ ТЕСТЫ===========
@pytest.mark.positive
def test_add_new_projects():
    # Получить список проектов
    body = get_projects_list()  # Получаем полный ответ API
    projects_before = body['content']  # Извлекаем список проектов
    len_before = len(projects_before)
    # Создание проекта
    result = create_projects("Проект1")
    new_id = result["id"]
    # Получить список проектов
    body = get_projects_list()
    projects_after = body['content']
    len_after = len(projects_after)

    assert len_after - len_before == 1
    assert projects_after[-1]["id"] == new_id


@pytest.mark.positive
def test_get_project():
    # Создание проекта
    result = create_projects("Проект2")
    new_id = result["id"]
    # Получить компанию по id
    new_project = get_projects(new_id)

    assert new_project['id'] == new_id
    assert new_project['title'] == "Проект2"


@pytest.mark.positive
def test_edit_project():
    result = create_projects("Старое название")
    new_id = result["id"]

    new_title = "Название изменено"
    edit_project = edit(new_id, new_title)

    assert edit_project['id'] == new_id


# ===========НЕГАТИВНЫЕ ПРОВЕРКИ===============
@pytest.mark.negative
def test_get_nonexistent_project():
    nonexistent_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(base_url + '/projects/' + nonexistent_id, headers=my_headers)

    assert response.status_code == 404, \
        f"Ожидалась ошибка 404, получен {response.status_code}. Ответ: {response.text}"


@pytest.mark.negative
def test_create_project_invalid_data():
    # Попытка создания проекта без названия
    invalid_project = {}
    response = requests.post(base_url + '/projects', json=invalid_project, headers=my_headers)

    assert response.status_code in [400], \
        f"Ожидалась ошибка 400, получен {response.status_code}. Ответ: {response.text}"


@pytest.mark.negative
def test_create_project_without_auth():
    project = {
        "title": "Новый проект без авторизации"
    }
    response = requests.post(base_url + '/projects', json=project)
    assert response.status_code in [401], \
        f"Ожидалась ошибка 401, получен {response.status_code}. Ответ: {response.text}"


@pytest.mark.negative
def test_edit_nonexistent_project():
    project = {
        "title": "new project"
    }
    nonexistent_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(base_url + '/projects/' + nonexistent_id, headers=my_headers, json=project)

    assert response.status_code == 404, \
        f"Ожидалась ошибка 404, получен {response.status_code}. Ответ: {response.text}"
