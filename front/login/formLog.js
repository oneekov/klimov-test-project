document.getElementById('LogForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Отменяем стандартную отправку формы

    // Собираем данные формы
    const formData = {
        username: document.getElementById('name').value,
        password: document.getElementById('password').value
    };

    try {
        //window.location.href = "./main.html"; 
        // Отправляем POST-запрос
        const response = fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Указываем тип данных
            },
            body: JSON.stringify(formData) // Конвертируем объект в JSON
        });

        // Обрабатываем ответ
        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }

        const result = response.json(); // Парсим JSON-ответ
        document.getElementById('responseMessage').textContent = "Успешно! Ответ: " + JSON.stringify(result);
        document.location.href = "./main.html"

    } catch (error) {
        //console.error('Ошибка:', error);
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
