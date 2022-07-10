# Проект CRUD для Yatube
## _Описание_
API доступен только аутентифицированным пользователям. Аутентификация по токену **TokenAuthentication**.    
Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.   
При попытке изменить чужие данные возвращается код ответа **403 Forbidden**.   

Для взаимодействия с ресурсами описаны и настроены такие **эндпоинты**:
- ***api/v1/api-token-auth/ (POST)***: передаём логин и пароль, получаем токен.
- ***api/v1/posts/ (GET, POST)***: получаем список всех постов или создаём новый пост.
- ***api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)***: получаем, редактируем или удаляем пост по **id**.
- ***api/v1/groups/ (GET)***: получаем список всех групп.
- ***api/v1/groups/{group_id}/ (GET)***: получаем информацию о группе по **id**.
- ***api/v1/posts/{post_id}/comments/ (GET, POST)***: получаем список всех комментариев поста с **id=post_id** или создаём новый, указав **id** поста, который хотим прокомментировать.
- ***api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)***: получаем, редактируем или удаляем комментарий по **id** у поста с **id=post_id**.

## Технологии
- Python 3.7.9
- Django 2.2.16
- Django Rest Framework 3.12.4
- Pytest 6.2.4
- Pytest-django 4.4.0
- Pytest-pythonpath 0.7.3
- Requests 2.26.0
- Pillow 8.3.1
- Sorl-thumbnail 12.7.0

## Установка
1. **Клонируйте репозиторий:**
```sh
git clone https://github.com/Alexandra1624/api_yatube.git
```

2. **Cоздать и активировать виртуальное окружение:**
```sh
python -m venv venv
source venv/Scripts/activate
```

3. **Обновить pip и установить зависимости из файла requirements.txt:**
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. **Выполнить миграции:**
```sh
cd yatube_api
python manage.py migrate
```

5. **Создать суперпользователя:**
```sh
python manage.py createsuperuser
```

6. **Проверка тестов:**
```sh
pytest
```

7. **Запустить проект:**
```sh
python manage.py runserver
```
Сервер запущен на странице:     
http://localhost:8000       

 ## Автор

**_Александра Радионова_**  
https://github.com/Alexandra1624  
https://t.me/alexandra_R1624  
sashamain@yandex.ru

