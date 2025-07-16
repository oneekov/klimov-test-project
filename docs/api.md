# Описание API методов
*Без Swagger = без сваги :(*

**Все методы API имеют общий эндпоинт /api/**
## POST /api/send_results
Тело запроса:
```json
{
    "person": {
        "sex": "male", // male/female
        "age": 21, // от 0 до 120
        "full_name": ["Ivanov", "Ivan", "Ivanovich"] // в формате ФИО, лимит на каждую часть 40 символов
    },
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
{"status": "error", "error": "error here"}
```