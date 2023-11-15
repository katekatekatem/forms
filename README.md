### **Описание проекта:**

Web-приложение для определения заполненных форм.


### **Используемые технологии:**

Python, 
Django, 
REST API


### **Автор проекта:**

Екатерина Мужжухина, e-mail: muzhzhukhina@mail.ru, https://github.com/katekatekatem
Резюме: https://hh.ru/resume/2a6d13b3ff0c5ff8960039ed1f4f5959364c43?hhtmFrom=resume_list


### **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

> git clone git@github.com:katekatekatem/forms.git
> 
> cd forms

Cоздать и активировать виртуальное окружение:

> python -m venv venv
> 
> source venv/scripts/activate

Установить зависимости из файла requirements.txt:

> python -m pip install --upgrade pip
> 
> pip install -r requirements.txt

Выполнить миграции:

> python manage.py migrate

Выполнить тесты:

> python manage.py test

Запустить проект:

> python manage.py runserver
