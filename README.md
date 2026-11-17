@"
# Django Project

Учебный проект на фреймворке Django. Управление зависимостями через Poetry, разработка по **GitFlow**.

## Установка и запуск

1. Клонируйте репозиторий и установите зависимости:
   ``````bash
   poetry install
   ``````
2. Примените миграции и запустите сервер:
   ``````bash
   poetry run python manage.py migrate
   poetry run python manage.py runserver
   ``````

## Правила работы с Git (GitFlow)
* `main` — стабильная ветка с готовым кодом.
* `develop` — основная ветка разработки.
* `feature/homework-N` — ветки для выполнения домашних заданий (создаются от `develop`).
"@ | Out-File -FilePath README.md -Encoding utf8