from django.db import models
from users.models import User
import uuid

# Create your models here.
class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    writer = models.ForeignKey(User,verbose_name='작성자', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='작성시간', auto_now_add=True)
    title = models.CharField(verbose_name='제목', max_length=200)
    content = models.TextField(verbose_name='내용')
    ai_feedback = models.TextField(verbose_name='왓셩 피드백')


class PostLike(models.Model):
    postlike_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    liked_post = models.ForeignKey(Post,verbose_name='좋아요 게시글', on_delete=models.CASCADE)
    like_user = models.ForeignKey(User, verbose_name='좋아요 유저', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='좋아요 시간',auto_now_add=True)