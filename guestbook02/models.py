from django.db import models

# Create your models here.

class Guestbook(models.Model):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    message = models.CharField(max_length=4000)
    regdate = models.DateTimeField(auto_now=True)
    #reg date에 대한 포맷팅 설정 해줘야 함

    def __str__(self):
        return f"Guestbook : {self.name}, {self.password}, {self.message}, {self.regdate}"