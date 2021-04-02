
# [Django Practice]

## ▶︎ Making django project and Setting
### 1. Making new pycharm project
### 2. Install django (terminal) :
```terminal
(venv) # pip install django
```
### 3. Install mysqlclient (on macbook, 3.x python)
```terminal
(venv) # pip install mysql-connector-python
(venv) # pip install pymysql
```

### 4. Making new django project
```terminal
(venv) # django-admin startproject django_practice
```
### 5. Organize folder
### 6. Set default setting (settings.py)
1) time zone (locale, rec. capital)
```python
TIME_ZONE = "ASIA/SEOUL"
```
2) database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webDB',
        'USER': 'webDB',
        'PASSWORD': 'webDB',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```
3) import pymysql
```python
import pymysql
pymysql.install_as_MySQLdb()
```
### 7. Making django project control app DB
```terminal
(venv) # python manage.py makemigrations
(venv) # python manage.py migrate
```
cf ) mysql 5.x error / add on manage.py
```python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```

### 8. Create superuser for project
```terminal
(venv) # python manage.py createsuperuser
```


### 9. Reconfirm all settings
1) running server
```terminal
(venv) # python manage.py runserver 0.0.0.0:9999
```
2) check thru browser
- url http://localhost:9999
- log in with admin (password)

## ▶︎ Append application on django project
### 1. Making integrated template directory 

1) make folder : template
2) add settings.py
```python
'DIRS' : [os.path.join(BASE_DIR, 'templastes')]
```
### 2. Making (helloworld) application
1) make application
```terminal
(venv) # python manage.py startapp helloworld
```
2) registry application (settings.py) 
```python
INSTALLED_APPS = [
    'helloworld',
]
```
3) add application directory on template

4) setting urls 
```python
urlpatterns = [
    path('hello1/', helloworld.views.hello1),
]
```
5) repeat
