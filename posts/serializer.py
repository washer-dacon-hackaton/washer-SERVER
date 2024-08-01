from .models import Post
from rest_framework import serializers
from users.models import User
from .ai_feedback import ai_feedback

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'writer', 'created_at', 'title', 'content', 'ai_feedback']
        read_only_fields = ['writer', 'ai_feedback']

    def create(self, validated_data):
        request = self.context.get('request')
        nickname = self.context.get('nickname')
        user = User.objects.get(nickname=nickname) # 작성자를 현재 로그인한 사용자로 설정
        validated_data['writer'] = user

        # AI 피드백 생성
        ai_feedback = self.get_ai_feedback(validated_data['title'], validated_data['content'])
        validated_data['ai_feedback'] = ai_feedback

        return super().create(validated_data)

    def get_ai_feedback(self, title, content):
        message=f"title : {title}\n content : {content}"
        return ai_feedback(message)    