from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
# Create your views here.
#로그인 API
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        # 이메일과 비밀번호가 제공되지 않은 경우
        if not email or not password:
            return Response({"success":False, 
                            "message": "이메일과 비밀번호를 모두 제공해야 합니다."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # 이메일을 사용하여 사용자 검색
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"success":False,
                            "message": "해당 이메일의 사용자를 찾을 수 없습니다."}, 
                            status=status.HTTP_404_NOT_FOUND)

        # 비밀번호 확인
        if not user.password ==password:
            return Response({"success":False,
                            "message": "비밀번호가 올바르지 않습니다."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # 인증 성공
        return Response({"success":True, "message": "로그인 성공!","nickname":user.nickname}, status=status.HTTP_200_OK)