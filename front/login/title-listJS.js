// Базовый JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Страница загружена!');
    
    // Пример обработчика событий
    const links = document.querySelectorAll('nav a');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            console.log('Нажата ссылка: ' + e.target.textContent);
        });
    });
});