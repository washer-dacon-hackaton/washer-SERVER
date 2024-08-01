from .models import Dairy,Question
from rest_framework import serializers
from users.models import User
from .models import Dairy
from posts.ai_feedback import ai_feedback
from .color_print import analyze_emotions_using_words_df1, analyze_emotions_using_words_df2, rgb_to_hex

class DairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['dairy_id', 'user', 'sadness','love','anger','joy','gratitude','fear','emotion_color','bright_color','created_at']
        read_only_fields = ['user','sadness','love','anger','joy','gratitude','fear','emotion_color','bright_color']
    def create(self, validated_data):
        # user를 직접 할당
        user_id = self.context['user_id']
        user=User.objects.get(user_id=user_id)# View에서 컨텍스트로 전달받은 user
        validated_data['user'] = user
        # validated_data에서 직접 값을 추출하여 할당
        validated_data['sadness']=self.context['data']['sadness']
        validated_data['love']=self.context['data']['love']
        validated_data['anger']=self.context['data']['anger']
        validated_data['joy']=self.context['data']['joy']
        validated_data['gratitude']=self.context['data']['gratitude']
        validated_data['fear']=self.context['data']['fear']
        validated_data['emotion_color']=self.context['data']['emotion_color']
        validated_data['bright_color']=self.context['data']['bright_color']
        
        return super().create(validated_data)
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['question_id','special_joy','weather','self_praise','highlight','dairy_feedback']
        fead_only_fields=['dairy_feedback']

    def create(self, validated_data):
        request = self.context.get('request')
        nickname = self.context.get('nickname')
        dairy_id = self.context['dairy_id']
        print(dairy_id)

        special_joy = request.data.get('special_joy')
        weather = request.data.get('weather')
        self_praise = request.data.get('self_praise')
        highlight = request.data.get('highlight')

        '''
        emotion_keywords = request.data.get('emotion_keywords')
        # 감정 단어를 카테고리별로 분류하고, 색상을 도출하는 함수 호출
        category_counts, emotion_color = analyze_emotions_using_words_df1(emotion_keywords)
        emotion_color=rgb_to_hex(emotion_color)
        bright_color = analyze_emotions_using_words_df2(emotion_keywords)
        bright_color=rgb_to_hex(bright_color)
        '''



        # 사용자 인스턴스를 nickname으로 가져옴 (이 예제에서는 User 모델에 nickname 필드가 있다고 가정)
        user = User.objects.get(nickname=nickname)
        dairy=Dairy.objects.get(dairy_id=dairy_id)
        message=f"오늘의 날씨는 어땠나요? 그 날씨를 즐길 수 있었던 방법이 있었나요?\n{weather}\n오늘 자신에게 칭찬해주고 싶은 일이 있나요?\n{self_praise}\n오늘 당신만이 누린 소소하지만 특별한 순간은 무엇이었나요?\n{special_joy}\n오늘 산책이나 외출 중에 본 가장 아름다운 것은 무엇이었나요?\n{highlight}"
        print('a')
        question=Question.objects.create(
            dairy=dairy,
            special_joy=special_joy,
            weather=weather,
            self_praise=self_praise,
            highlight=highlight,
            dairy_feedback=ai_feedback(message)
        )
        print('b')



        return question

