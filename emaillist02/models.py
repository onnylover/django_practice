from django.db import models

# Create your models here.

class Emaillist(models.Model):
    # pk는 자동 생성
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f"Emaillist({self.first_name},{self.last_name},{self.email})"