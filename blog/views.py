from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

'''
전체 블로그를 조회 
'''

#@ - 함수를 보조해주는 역할, 따로 기능은 없음 
#@api_view(['GET','POST']) #GET 요청만 받겠다 
#@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticatedOrReadOnly])


# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True) #Post 모델들을 직렬화할 수 있음 #하나가 아닌 여러 데이터를 직렬화하는 경우 'many=True' 옵션
#         return Response(serializer.data, status=status.HTTP_200_OK) # 직렬화된 데이터(serializer.data)를 가지고 Response 만들어서 반환
#         #요청이 처리되었고 처리완료된 결과로 status HTTP 200 을 보내는 것 
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(): # 유효성 검사 #ex. title의 경우는 max_length=100인데 길이 200인게 들어오면 false로 반환 
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class BlogList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        blogs = Post.objects.all() #Blog 대신 post
        serializer = PostSerializer(blogs, many=True) #blog 대신 post
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data) #post 
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



'''
한 블로그 조회
'''

class BlogDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        blog = get_object_or_404(Post, pk=pk) #post
        return blog

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = PostSerializer(blog) #post 
        return Response(serializer.data)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = PostSerializer(blog, data=request.data) #post
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','PUT','DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsOwnerOrReadOnly])
# def post_detail(request,pk): # 요청 데이터와 함께 pk값도 url을 통해 받겠다 #pk는 url에 포함된 값, 인자 (반드시 같이 적어줘야 함) ex. www. ~ /get/1 -> 1번이 pk
#     try:
#         post = Post.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = PostSerializer(post) #하나의 블로그 데이터를 조회하기 때문에 many=True 옵션은 없음
#             return Response(serializer.data,status= status.HTTP_200_OK)
#         elif request.method =='PUT':
#             serializer = PostSerializer(post,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             post.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     #pk값을 가지고 post를 찾는데 만약 100번째 post가 없다면? -> 404 에러를 띄우게 함     
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    