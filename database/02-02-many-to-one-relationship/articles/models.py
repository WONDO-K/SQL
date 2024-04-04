from django.db import models
from django.conf import settings
from accounts.models import User


# Create your models here.
class Article(models.Model):
    # models.py가 실행되는 시점에 User 객체가 없어서 에러가 발생함
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # 그래서 일단 문자열로 설정하여 참조할 수 있게 함
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
