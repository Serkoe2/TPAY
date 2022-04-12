Структура проекта

- app
-- models Модели БД
-- routers Роутинг Приложения
---- orders.py API
---- view.py Пользовательский интерфейс
-- schemas Схемы запросов
-- utils Контроллеры между роутингом и моделями
---- Order.py Класс для работы с сущностью заказ
---- TinkoffApi.py Класс для работы с API Tinkoff
-- db_config.py Конфиг БД
-- main.py Entrypoint приложения
- migrations папка с миграциями бд
- static директория со статикой
- templates директория с html шаблонами
-- index.html
- alembic.ini конфиг alembic
- docker-compose.yml Сборка для docker-compose
- Makefile
- Procfile для деплоя на Heroku
- requirements.txt файл с зависимостями
- runtime.txt версия Python для Heroku

Приложение позволяет создать заказ, узнать статус, и изменить его (Например Подтвердить или Отменить заказ)
Все заказы вынесены на общую страницу

Демо https://pacific-chamber-19664.herokuapp.com/

