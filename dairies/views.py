from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import Dairy,Question
from .serializer import DairySerializer, QuestionSerializer
from datetime import datetime
from .color_print import analyze_emotions_using_words_df1, analyze_emotions_using_words_df2, rgb_to_hex

class DairyCreateView(APIView):
    def get(self, request, *args, **kwargs):
        #시간 기준 오늘꺼 있으면, ai feedback, colors보여주고, 없으면, 없다고 말하기
        # 쿼리 파라미터로 날짜 받기
        date_str = request.query_params.get('date')
        query_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        
        # 사용자 닉네임 받기
        nickname = self.kwargs.get('nickname')

        # 해당 날짜와 사용자에 대한 Dairy 객체 조회
        try:
            dairy = Dairy.objects.filter(user__nickname=nickname, created_at__date=query_date).order_by('-created_at').first()
        except Dairy.DoesNotExist:
            return Response({"message": "아직 오늘 작성된 일기가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        question=dairy.question
        print(question)
        return Response({"dairy_feedback": question.dairy_feedback,
                "emotion_color": dairy.emotion_color,
                "bright_color": dairy.bright_color})

    def post(self, request, *args, **kwargs):
        # 사용자가 요청한 감정 단어 리스트를 가져옴
        emotion_keywords = request.data.get('emotion_keywords', [])
        
        # 감정 단어를 카테고리별로 분류하고, 색상을 도출하는 함수 호출
        category_counts, emotion_color = analyze_emotions_using_words_df1(emotion_keywords)
        emotion_color=rgb_to_hex(emotion_color)
        bright_color = analyze_emotions_using_words_df2(emotion_keywords)
        bright_color=rgb_to_hex(bright_color)
        # Dairy 모델 인스턴스 생성
        nickname = self.kwargs.get('nickname')
        user = User.objects.get(nickname=nickname)  # 사용자 찾기
        

        dairy_data = {
            #'user': user,
            'sadness': category_counts['슬픔'],
            'love': category_counts.get('사랑', 0),
            'anger': category_counts.get('분노', 0),
            'joy': category_counts.get('기쁨', 0),
            'gratitude': category_counts.get('감사', 0),
            'fear': category_counts.get('공포', 0),
            'emotion_color': emotion_color,
            'bright_color': bright_color
        }
        serializer = DairySerializer(data=dairy_data, context={'user_id':user.user_id, 'data':dairy_data})
        if serializer.is_valid():
            dairy = serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 시리얼라이저를 통해 데이터 검증 및 저장

        serializer = QuestionSerializer(data=request.data, context={'request': request, 'nickname': nickname, 'dairy_id':dairy.dairy_id})
        
        if serializer.is_valid():
            question = serializer.save()
            return Response({'question_id':question.question_id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
