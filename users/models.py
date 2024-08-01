from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    password=models.CharField(verbose_name='비밀번호',max_length=255,default='12341234')
    created_at = models.DateTimeField(verbose_name='가입시간', auto_now_add=True)
    name = models.CharField(verbose_name='이름',max_length=255)
    nationality = models.CharField(verbose_name='국적',max_length=255)
    email = models.EmailField(verbose_name='이메일',unique=True)
    nickname = models.CharField(verbose_name='닉네임',max_length=255, unique=True)

