# План API Ендпоінтів (API Endpoints Design)
Проєкт: CRM для Навчального Центру

1. Користувачі та Авторизація (Users & Auth)
- POST /api/auth/login/ — Вхід у систему (отримання токена за номером телефону та паролем).
- POST /api/auth/register/ — Реєстрація нового співробітника/адміністратора.
- GET /api/auth/me/ — Отримання профілю поточного авторизованого користувача.

2. Філії (Branches)
- GET /api/branches/ — Отримати список усіх філій.
- POST /api/branches/ — Створити нову філію.
- GET /api/branches/<id>/ — Отримати деталі конкретної філії.
- PUT /api/branches/<id>/ — Оновити дані філії.
- DELETE /api/branches/<id>/ — Видалити філію (архівувати).

3. Предмети (Subjects)
- GET /api/subjects/ — Отримати список усіх предметів.
- POST /api/subjects/ — Додати новий предмет.
- GET /api/subjects/?branch_id=<id> — Отримати список предметів конкретної філії.

4. Студенти (Students)
- GET /api/students/ — Отримати список усіх студентів.
- POST /api/students/ — Створити картку нового студента.
- GET /api/students/<id>/ — Отримати профіль студента.
- PUT /api/students/<id>/ — Редагувати дані студента (наприклад, змінити телефон).
- GET /api/students/?branch_id=<id> — Отримати список студентів певної філії.

5. Групи (Groups)
- GET /api/groups/ — Отримати список усіх груп.
- POST /api/groups/ — Створити нову групу.
- POST /api/groups/<id>/add_student/ — Додати студента до групи.