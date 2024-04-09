from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 자기 자신과 관계를 맺을 때 self,
    # symmetrical 대칭관계
    followings = models.ManyToManyField('self',symmetrical=False, related_name='followers')
