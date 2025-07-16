# klimov-test-project
[Описание API](./docs/api.md)
## Развёртывание
1. Скопировать .env.template в .env и вписать свои параметры
2. Использовать yml для разработки: `docker compose up -d --build`
*Проброшена БД наружу, упрощён компоуз*
Для продакшена: `docker compose -f docker-compose.prod.yml up -d --build`
