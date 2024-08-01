from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializer import PostSerializer
from .models import Post,PostLike
from users.models import User

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        # Nickname을 URL에서 가져오기
        nickname = self.kwargs.get('nickname')
        
        # 시리얼라이저에 context 추가
        serializer = self.get_serializer(data=request.data, context={'request': request, 'nickname': nickname})
        serializer.is_valid(raise_exception=True)
        
        # 저장 및 응답 생성
        self.perform_create(serializer)
        return Response({'message':'게시글 작성 완료','post_id':serializer.instance.post_id}, status=status.HTTP_201_CREATED)

    def get(self,request, *args, **kwargs):
        post_id = request.data.get('post_id')
        try:
            # post_id로 Post 객체 조회
            post = Post.objects.get(post_id=post_id)
        except Post.DoesNotExist:
            return Response({'error': '해당 post_id를 가진 게시글이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Post 객체를 시리얼라이즈하여 응답 생성
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self,request, *args, **kwargs):
        nickname = self.kwargs.get('nickname')
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(post_id=post_id)  # 게시글 찾기
            user = User.objects.get(nickname=nickname)  # 사용자 찾기
        except (Post.DoesNotExist, User.DoesNotExist):
            return Response({'error': '게시글이나 사용자를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        user_liked = PostLike.objects.filter(like_user=user, liked_post=post).exists()

        if user_liked:
            # 좋아요가 이미 존재하면 삭제
            user_liked.delete()
            return Response({'message': '취소'}, status=status.HTTP_204_NO_CONTENT)
        else:
            # 좋아요가 없으면 추가
            PostLike.objects.create(like_user=user, liked_post=post)
            return Response({'message': '나까지 행복해졌어요!'}, status=status.HTTP_201_CREATED)