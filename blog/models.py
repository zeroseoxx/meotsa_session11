from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Post(models.Model):  #게시글 
    user = models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE) #forigen key - 외래키 , Null을 허용하지 않으면 지난번에 작성한 게시글에 문제가 생겨서 null=True해줌 
    title = models.CharField(max_length=100) #CharField - 글(제목) 작성, 최대길이 지정해줘야함
    body = models.TextField(default="") #TextField - 무제한 문자
    date = models.DateTimeField(auto_now_add=True) #DateTimeField - 시간,날짜 저장/ Auto now add - add될 때만 자동저장 

    def __str__(self):
        return self.title
    