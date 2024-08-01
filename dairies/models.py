from django.db import models
from users.models import User
from posts.models import Post
import uuid

class Dairy(models.Model):
    dairy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE)
    dairy_feedback = models.TextField(verbose_name='왓셩 피드백')
    created_at = models.DateTimeField(verbose_name='작성시간', auto_now_add=True)

class DairyKeyword(models.Model):
    dairykeyword_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dairy = models.ForeignKey(Dairy, verbose_name='감정일기', on_delete=models.CASCADE, related_name='keywords')
    keyword = models.CharField(verbose_name='감정키워드', max_length=255)

class Question(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dairy = models.OneToOneField(Dairy, on_delete=models.CASCADE, related_name='question')
    weather = models.TextField(verbose_name='날씨 질문')
    self_praise = models.TextField(verbose_name='자기 칭찬')
    special_joy = models.TextField(verbose_name='특별 순간')
    highlight = models.TextField(verbose_name='하이라이트')