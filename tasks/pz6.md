## Практическое занятие №6. Работа веб-фреймворком flask

### Рассматриваемые вопросы
1. flask
2. jinja2

### 
Смотрите \\\\fs\\Кафедры\\732\\python\\flask\\flask.html

Создадим hello world на flask. Для этого в файле web.py напишите:

```python
from flask import Flask
app = Flask(__name__)  # это flask WSGI-приложение

# для нашего приложения есть декоратор, который обеспечивает привязку URL к функции
# при заходе на website/ будет выполнена функция hello_world
@app.route('/')
def hello_world():
    return 'Hello, World!'
```
Запустите веб-сервер flask. **Внимание** - такой запуск веб-сервера годится только для разработки. Он однопоточный и медленный. Для запуска на реальных пользователях требуется запустить полноценный веб-сервер, например, nginx. Или более простой в настройке gunicorn. В документации к flask это описано.

```bash
FLASK_APP=flask.py flask run
```
Ознакомьтесь с работой маршрутизации 

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

Создайте страничку с формами ввода фамилии и заданным вопросом с radiobutton выбора.