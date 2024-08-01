from django.contrib import admin
from .models import MonthlyReport,Wordcloud,HappyGraph,Hexagonal

@admin.register(MonthlyReport)
class MonthlyReportAdmin(admin.ModelAdmin):
    list_display=['monthlyreport_id','user','created_at','month_score','monthly_feedback']
# Register your models here.


'''
@admin.register(HappyGraph)
class HappyGraphAdmin(admin.ModelAdmin):
    list_display=[]
'''
