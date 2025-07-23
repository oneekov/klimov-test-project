# Описание API методов
*No Swagger = No Swag :(*

**Все методы API имеют общий эндпоинт /api/**
## POST /api/auth/register
Регистрация

Тело запроса:
```json
{
    "username": "johndoe",
    "password": "123123123", // от 8 символов
    "school": "School №3",
    "grade": [9, "A"], //1 - класс, 2 - буква класса
    "sex": "male", // male/female
    "age": 21, // от 0 до 120
    "full_name": ["Ivanov", "Ivan", "Ivanovich"], // в формате ФИО, лимит на каждую часть 40 символов
    "email": "123@gmail.com", // Проверка на email, может отсутствовать
    "number": "+79871234567" // может отсутствовать
}
```
Ответ:

201:
```json
{"status": "ok", "token": "123abc_access_token_here_123abc"}
```
400:
```json
{"status": "error", "message": "error here"}
```
409:
```json
{"status": "error", "message": "account already exist"} // сверка по username и email
```
## POST /api/auth/login
Логин

Тело запроса:
```json
{"username": "johndoe", "password": "123123123"}
```
Ответ:

200:
```json
{"status": "ok", "token": "123abc..."}
```
400:
```json
{"status": "error", "message": "creds not provided"}
```
401:
```json
{"status": "error", "message": "bad creds provided"}
```
404:
```json
{"status": "error", "message": "user not exist"}
```
## GET /api/me
Получение информации о текущем пользователе

Требует заголовка Authorization: Bearer Token

Ответ:

200:
```json
{
    "user": { // !!! Все значения, кроме id, is_admin, is_super_admin могут быть null !!!
        "age": 21,
        "contact_email": "123@gmail.com",
        "contact_number": "+79871234567",
        "grade_letter": "A",
        "grade_number": 9,
        "id": 2,
        "is_admin": true,
        "is_super_admin": false,
        "name": "Ivan",
        "patronymic": "Ivanovich",
        "school": "School №3",
        "sex": "male",
        "surname": "Ivanov"
    }
}
```
## POST /api/send_results
Отправка результатов

Требует заголовка Authorization: Bearer Token

Тело запроса:
```json
{
    "results": { // могут быть от -20 до 20
        "nature": -10, // Человек-природа
        "tech": 10, // Человек-техника
        "human": 5, // Человек-человек
        "sign_system": 2, // Человек-знаковая система
        "image": -5 // Человек-художественный образ
    }
}
```
Ответ:

200:
```json
{"status": "ok"}
```
400:
```json
{"status": "error", "message": "error here"}
```
## GET /api/admin/users/
Получение всех пользователей (не админов)

Тело запроса:
```
http://site_url/api/admin/users/?offset=0&limit=50

# offset - смещение
# limit - кол-во (макс. 50, стандарт. 50)
```

Требует заголовка Authorization: Bearer Token и наличия is_admin/is_superadmin у пользователя
Ответ:

200:
```json
{
    "users": [
        {
            "age": 21,
            "contact_email": "123@gmail.com",
            "contact_number": "+79871234567",
            "grade_letter": "A",
            "grade_number": 9,
            "id": 2,
            "is_admin": false,
            "is_super_admin": false,
            "name": "Ivan",
            "patronymic": "Ivanovich",
            "school": "School №3",
            "sex": "male",
            "surname": "Ivanov"
        },
        {
            // и другие...
        }
    ]
}
```
403 (нет прав):
```json
{"status": "error", "message": "access denied"}
```
## GET /api/admin/admins
Получение всех админов

Требует заголовка Authorization: Bearer Token и наличия is_superadmin у пользователя
Ответ:

200:
```json
{
    "admins": [
        { // !!! Все значения, кроме id, is_admin, is_super_admin могут быть null !!!
            "age": 21,
            "contact_email": "123@gmail.com",
            "contact_number": "+79871234567",
            "grade_letter": "A",
            "grade_number": 9,
            "id": 2,
            "is_admin": true,
            "is_super_admin": false,
            "name": "Ivan",
            "patronymic": "Ivanovich",
            "school": "School №3",
            "sex": "male",
            "surname": "Ivanov"
        },
        {
            // и другие...
        }
    ]
}
```
403 (нет прав):
```json
{"status": "error", "message": "access denied"}
```
## GET /api/admin/answers/csv/
Тело запроса:
```
http://site_url/api/admin/answers/csv/?school=52 школа&grade_number=9&profession_type=nature&offset=0&limit=50

# school - точное название школы
# grade_number - номер класса
# profession_type - тип профессии; возможные значения: ['nature', 'tech', 'human', 'sign_system', 'image']
```
Требует заголовка Authorization: Bearer Token и наличия is_admin/is_superadmin у пользователя

Ответ:

200:

*будет отдан файл .csv*

403 (нет прав):
```json
{"status": "error", "message": "access denied"}
```
## GET /api/admin/answers/excel/
Тело запроса:
```
http://site_url/api/admin/answers/excel/?school=52 школа&grade_number=9&profession_type=nature&offset=0&limit=50

# school - точное название школы
# grade_number - номер класса
# profession_type - тип профессии; возможные значения: ['nature', 'tech', 'human', 'sign_system', 'image']
```
Требует заголовка Authorization: Bearer Token и наличия is_admin/is_superadmin у пользователя

Ответ:

200:

*будет отдан файл .xlsx*

403 (нет прав):
```json
{"status": "error", "message": "access denied"}
```
## PATCH /admin/admins/rights/<id>
Изменение прав администратора/пользователя

id: ID пользователя, которому нужно изменить права

Тело запроса:
```json
{
  "is_admin": true,
  "is_super_admin": false
}
```

Требует заголовка Authorization: Bearer Token и наличия is_superadmin у пользователя

Ответ:

200:

```json
{"status": "ok", "message": "rights updated successfully"}
```

400:

```json
{"status": "error", "message": "data not provided"}
```

403:

```json
{"status": "error", "message": "access denied"}
```

404:

```json
{"status": "error", "message": "user not found"}
```