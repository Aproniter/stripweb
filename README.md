<h1 align="center">StripWeb</h1>


### Технологии
Python
Django
Docker
Strip


### Запуск проекта в dev-режиме
- В папке stripweb запустите docker контайнер:
    - sudo docker build -t stripweb . && sudo docker run -d -p 80:8000 stripweb

- Создайте суперпользователя:
    - sudo docker exec -it stripweb python manage.py createsuperuser

### Description
Проект, для тестирования API платежной системы https://stripe.com/.