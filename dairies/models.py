from django.db import models
from users.models import User
from posts.models import Post
import uuid

class Dairy(models.Model):
    dairy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE)
    sadness=models.IntegerField(verbose_name='슬픔빈도',default=0)
    love=models.IntegerField(verbose_name='사랑빈도',default=0)
    anger=models.IntegerField(verbose_name='분노빈도',default=0)
    joy=models.IntegerField(verbose_name='기쁨빈도',default=0)
    gratitude=models.IntegerField(verbose_name='감사빈도',default=0)
    fear=models.IntegerField(verbose_name='공포빈도',default=0)
    emotion_color = models.CharField(verbose_name='색조RGB',max_length=7,default='')  # 예: '#RRGGBB'
    bright_color = models.CharField(verbose_name='명도RGB',max_length=7,default='')   # 예: '#RRGGBB'
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
    dairy_feedback = models.TextField(verbose_name='왓셩 피드백',default='')