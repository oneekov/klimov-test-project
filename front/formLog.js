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
        document.getElementById('responseMessage').textContent = "Ошибка: " + error.message;
    }
});
