from django.db import models
import uuid
from users.models import User

class MonthlyReport(models.Model):
    monthlyreport_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name='사용자', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='작성시간', auto_now_add=True)
    month_score = models.IntegerField(verbose_name='행복점수')
    monthly_feedback = models.TextField(verbose_name='한달 ai feedback')

class Wordcloud(models.Model):
    wordcloud_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    monthly_report = models.ForeignKey(MonthlyReport, on_delete=models.CASCADE, related_name='wordclouds')
    post_keyword = models.CharField(verbose_name='행복글 키워드', max_length=255)
    keyword_count = models.IntegerField(verbose_name='키워드 빈도수')

class Hexagonal(models.Model):
    hexagonal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    monthly_report = models.OneToOneField(MonthlyReport, on_delete=models.CASCADE, related_name='hexagonal')
    emo1 = models.IntegerField()
    emo2 = models.IntegerField()
    emo3 = models.IntegerField()
    emo4 = models.IntegerField()
    emo5 = models.IntegerField()
    emo6 = models.IntegerField()

class HappyGraph(models.Model):
    happygraph_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    monthly_report = models.ForeignKey(MonthlyReport, on_delete=models.CASCADE, related_name='happygraphs')
    post_date = models.DateTimeField(verbose_name='행복글 작성시간')
    post_score = models.IntegerField(verbose_name='행복글 행복점수')