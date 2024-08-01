from .models import Dairy
from rest_framework import serializers

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['dairy_id', 'user', 'sadness','love','anger','joy','gratitude','fear','emotion_color','bright_color','created_at']
        read_only_fields = ['user','sadness','love','anger','joy','gratitude','fear','emotion_color','bright_color']