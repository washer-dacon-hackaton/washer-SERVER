from django.contrib import admin
from .models import Dairy,DairyKeyword,Question

@admin.register(Dairy)
class DairyAdmin(admin.ModelAdmin):
    list_display=['dairy_id','user','dairy_feedback','created_at']

@admin.register(DairyKeyword)
class DairyKeywordAdmin(admin.ModelAdmin):
    list_display=['dairykeyword_id','dairy','keyword']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['question_id','dairy','weather','self_praise','special_joy','highlight']
