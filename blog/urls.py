from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view()), #path의 두번째 인자로 반드시 함수가 와야함. as_view()
    path('<int:pk>/', BlogDetail.as_view()),
]