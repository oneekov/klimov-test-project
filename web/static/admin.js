function logOut() {
    // Удаляем куку token, установив дату истечения в прошлом
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

    // Перенаправляем на главную страницу
    window.location.href = "/admin/login";
}

// Функция для получения значения куки по имени
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Основная функция проверки авторизации
function checkUserAuth() {
    const token = getCookie('token');

    // Если токен отсутствует, вызываем logOut
    if (!token) {
        logOut();
        return;
    }

    // Отправляем запрос с Bearer-токеном
    fetch('/api/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                logOut();
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Проверяем флаги пользователя
            const user = data?.user;
            if (user?.is_admin === false && user?.is_super_admin === false) {
                logOut();
            }
        })
        .catch(error => {
            console.error('Ошибка проверки авторизации:', error);
        });
}

function checkMe() {
    const token = getCookie('token');
    if (!token) {
        console.error('No token found');
        return Promise.reject('No token found');
    }

    return fetch('/api/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('User data:', data);
            return data; // Return the user data for further use
        })
        .catch(error => {
            console.error('Error fetching /api/me:', error);
            throw error; // Re-throw error for further handling
        });
}

// Вызываем проверку при загрузке страницы
document.addEventListener('DOMContentLoaded', checkUserAuth);