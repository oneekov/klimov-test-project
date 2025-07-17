# Описание API методов
*No Swagger = No Swag :(*

**Все методы API имеют общий эндпоинт /api/**
## POST /api/auth/register
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
    "email": "123@gmail.com", // Проверка на email
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
## POST /api/send_results
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