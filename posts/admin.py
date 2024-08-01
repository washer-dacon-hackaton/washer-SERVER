from django.contrib import admin
from .models import Post,PostLike
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['post_id','writer','created_at','title','content','ai_feedback']
