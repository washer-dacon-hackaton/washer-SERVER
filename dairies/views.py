from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .serializer import DiarySerializer
from .color_print import analyze_emotions_using_words_df1, analyze_emotions_using_words_df2, rgb_to_hex

class DairyCreateView(APIView):
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
            # 현재 로그인한 사용자
            'sadness': category_counts.get('슬픔'),
            'love': category_counts.get('사랑'),
            'anger': category_counts.get('분노'),
            'joy': category_counts.get('기쁨'),
            'gratitude': category_counts.get('감사'),
            'fear': category_counts.get('공포'),
            'emotion_color': emotion_color,  # 기본 색상
            'bright_color': bright_color     # 명도에 기반한 색상
        }
        
        # 시리얼라이저를 통해 데이터 검증 및 저장
        serializer = DiarySerializer(data=dairy_data)
        if serializer.is_valid():
            dairy = serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)