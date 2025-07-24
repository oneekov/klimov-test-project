document.getElementById('LogForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Отменяем стандартную отправку формы

    // Собираем данные формы
    const formData = {
        username: document.getElementById('name').value,
        password: document.getElementById('password').value
    };

    try {
        // Отправляем POST-запрос
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Указываем тип данных
            },
            body: JSON.stringify(formData) // Конвертируем объект в JSON
        });

        // Обрабатываем ответ
        const result = await response.json();

        if (!response.ok) {
            document.getElementById("error3").hidden = false;
            // Показываем сообщение об ошибке, если оно есть в ответе
            document.getElementById('responseMessage').value = result.message || `Ошибка HTTP: ${response.status}`;
            throw new Error(result.message || `Ошибка HTTP: ${response.status}`);
        }

        // Проверяем наличие токена и записываем его в куки
        if (result.token) {
            createCookie('auth_token', result.token, 1); // Сохраняем токен на 1 день
            console.log(getCookie('auth_token'));
        }

        console.log("Успешно! Ответ: " + JSON.stringify(result));
        document.location.href = "/login/main.html";

    } catch (error) {
        console.log("Ошибка: " + error.message);
    }
});

function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

window.addEventListener('DOMContentLoaded', function () {
    const token = getCookie('auth_token');
    if (token !== "") {
        window.location.href = '/test';
    }
});
