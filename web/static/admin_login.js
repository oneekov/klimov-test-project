async function login() {
    try {
        username = document.getElementById("login").value;
        password = document.getElementById("password").value;

        // Проверка наличия введенных данных
        if (!username || !password) {
            throw new Error('Пожалуйста, введите имя пользователя и пароль');
        }

        // Отправка запроса на /api/auth/login/
        const loginResponse = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "username": username, "password": password })
        });

        // Обработка возможных ошибок
        if (loginResponse.status === 401) {
            throw new Error('Неверные учетные данные');
        } else if (loginResponse.status === 404) {
            throw new Error('Пользователь не существует');
        } else if (!loginResponse.ok) {
            throw new Error(`Ошибка сервера: ${loginResponse.status}`);
        }

        // Получение токена из ответа
        const loginData = await loginResponse.json();
        const token = loginData.token;

        // Отправка запроса на /api/me/ с токеном
        const meResponse = await fetch('/api/me', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!meResponse.ok) {
            throw new Error('Не удалось получить данные пользователя');
        }

        const userData = await meResponse.json();

        // Проверка прав пользователя
        if (!userData.user.is_admin && !userData.user.is_super_admin) {
            throw new Error('Недостаточно прав для доступа');
        }

        // Сохранение токена в куки
        document.cookie = `token=${token}; path=/;expires=${new Date(Date.now() + 86400 * 1000).toUTCString()}`;

        window.location.href = './dashboard';

    } catch (error) {
        console.error(error);
        alert(error.message); // или любая другая обработка ошибки
    }
}