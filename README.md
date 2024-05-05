# ToDoList

ToDoList - это мощный и интуитивно понятный список дел, который поможет вам организовать свою жизнь и работу.

### Установка

Клонируйте репозиторий и перейдите в папку с проектом
```
git clone git@github.com:nepa27/list_todo.git
cd list_todo
```
Создайте **виртуальное окружение**
```
python3 -m venv venv
source venv/bin/activate    # (Ubuntu)
./venv/Scripts/python       # (Windows)
```
Затем установите необходимые зависимости из файла **requirements.txt**
```
pip install -r requirements.txt
```
Выполните миграции
```
python manage.py runserver
```

## Запуск

Перейдите в корневую директорию проекта, где находится файл **manage.py**
и запустите сервер
```
cd list_todo
python3 manage.py runserver
```
Если вы все правильно сделали, то высветится приглашение
```
System check identified no issues (0 silenced).
April 20, 2024 - 15:35:58
Django version 3.2.16, using settings 'list_todo.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Откройте браузер и перейдите по адресу **http://127.0.0.1:8000/**.

При возникновении ошибки
```
python: can't open file 'list_todo/manage.py'[Errno 2] No such file or directory
```
убедитесь, что вы находитесь в корневой директории проекта

### Инструменты и стек
#python #HTML #CSS #Django #Bootstrap #Pythonanywhere
