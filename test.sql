INSERT INTO klimov.users (
    username,
    password_hash,
    is_admin,
    is_super_admin,
    surname,
    name,
    patronymic,
    school,
    grade_number,
    grade_letter,
    contact_email,
    contact_number
)
SELECT
    -- username: user1, user2, ..., user25
    'user' || g.idx AS username,

    -- password_hash: заглушка (например, хеш пароля 'password')
    '$2b$12$KQjODeU0.eb8V9Z8vR8Y9tQ6I2X6V9Z8vR8Y9tQ6I2' AS password_hash,

    -- роли
    false AS is_admin,
    false AS is_super_admin,

    -- ФИО: случайные имена из списка
    (ARRAY['Иванов','Петров','Сидоров','Смирнов','Кузнецов','Попов','Васильев','Морозов','Фёдоров','Николаев'])[floor(random() * 10 + 1)] AS surname,
    (ARRAY['Иван','Петр','Алексей','Дмитрий','Сергей','Михаил','Владимир','Андрей','Евгений','Олег'])[floor(random() * 10 + 1)] AS name,
    (ARRAY['Иванович','Петрович','Алексеевич','Дмитриевич','Сергеевич','Михайлович','Владимирович','Андреевич','Евгеньевич','Олегович'])[floor(random() * 10 + 1)] AS patronymic,

    -- Школа: Школа № + число
    'Школа №' || (floor(random() * 50 + 1)::int) AS school,

    -- Класс: число от 1 до 11
    (floor(random() * 11 + 1)::int) AS grade_number,

    -- Буква класса: A-E
    (ARRAY['А','Б','В','Г','Д'])[floor(random() * 5 + 1)] AS grade_letter,

    -- Email: userN@example.com
    'user' || g.idx || '@example.com' AS contact_email,

    -- Номер: +7 (9XX) XXX-XX-XX
    '+79' || 
    floor(random() * 9)::int || 
    floor(random() * 9)::int || 
    '' || 
    floor(random() * 900 + 100)::int || 
    '' || 
    floor(random() * 90 + 10)::int || 
    '' || 
    floor(random() * 90 + 10)::int AS contact_number

FROM generate_series(1, 25) AS g(idx);

INSERT INTO klimov.answers (
    user_agent,
    ip,
    user_id,
    nature_points,
    tech_points,
    human_points,
    sign_points,
    image_points
)
SELECT
    '' AS user_agent,
    '' AS ip,
    FLOOR(RANDOM() * 25 + 2)::INTEGER AS user_id,  -- случайное число от 2 до 26
    FLOOR(RANDOM() * 11)::INTEGER AS nature_points,
    FLOOR(RANDOM() * 11)::INTEGER AS tech_points,
    FLOOR(RANDOM() * 11)::INTEGER AS human_points,
    FLOOR(RANDOM() * 11)::INTEGER AS sign_points,
    FLOOR(RANDOM() * 11)::INTEGER AS image_points
FROM generate_series(1, 70);
