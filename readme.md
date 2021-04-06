
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

## ▶︎ Make emaillist01 application (SQL Query)
### 1. Making integrated template directory
1) make application
```terminal
(venv) # python manage.py startapp emaillist01
```
2) registry application (settings.py) 
```python
INSTALLED_APPS = [
    'emaillist01',
]
```
3) add application directory on template as emaillist01

4) setting urls 
```python
urlpatterns = [
    path('emaillist01/', emaillist01.views.index),
]
```
5) repeat


## ▶︎ Make guestbook01 application
### 1. Making integrated template directory
1) make application
```terminal
(venv) # python manage.py startapp gustbook01
```
2) registry application (settings.py) 
```python
INSTALLED_APPS = [
    'guestbook01',
]
```
3) add application directory on template as guestbook01

4) setting urls 
```python
urlpatterns = [
    path('guestbook01/', guestbook01.views.index),
]
```
5) template filter
    - linebreakbr : "aaa\nbbb"  --|->  "aaa<br>bbb"
    
    - mathfilters
      - 설치
       ```terminal
       (venv) # pip install django-mathfilters
       ```
    - setting.py / apps
      ```python
      'mathfilters'
      ```
    - add on top of template 
       ```html
       {% load mathfilters %}
       ```
   
## ▶︎ Make emaillist02 application (ORM)
### 1. Making integrated template directory
1) make application
```terminal
(venv) # python manage.py startapp emaillist02
```
2) registry application (settings.py) 
```python
INSTALLED_APPS = [
    'emaillist02',
]
```
3) add application directory on template as emaillist02

4) make table and define of Model class
- define class
```python
class Emaillist(models.Model):
    # pk는 자동 생성
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f"Emaillist({self.first_name},{self.last_name},{self.email})"
```
- make table
```terminal
(venv) # python manage.py makemigrations
(venv) # python manage.py migrate
```

5) setting urls 
```python
urlpatterns = [
    path('emaillist02/', emaillist02.views.index),
]
```

## ▶︎ Make guestbook02 application (ORM)
### 1. Making integrated template directory
1) make application
```terminal
(venv) # python manage.py startapp guestbook02
```
2) registry application (settings.py) 
```python
INSTALLED_APPS = [
    'guestbook02',
]
```
3) add application directory on template as guestbook02

4) make table and define of Model class
- define class
```python
class Guestbook(models.Model):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    message = models.CharField(max_length=4000)
    regdate = models.DateTimeField(auto_now=True)
    #reg date에 대한 포맷팅 설정 해줘야 함

    def __str__(self):
        return f"Guestbook : {self.name}, {self.password}, {self.message}, {self.regdate}"
```
- make table
```terminal
(venv) # python manage.py makemigrations
(venv) # python manage.py migrate
```

5) setting urls 
```python
urlpatterns = [
    path('guestbook02/', guestbook02.views.index),
]
```