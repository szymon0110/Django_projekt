from django.urls import path 
from . import views


urlpatterns = [
    path('home/question/<int:qs_id>/',views.question_detail,name = "question"),
    path('home/',views.home, name="home"),
    path('home/login',views.LoginSite, name="login"),
    path('home/registration',views.SignUpSite, name='register'),
    path('home/logout',views.UserLogout, name="logout"),
    path('home/create_question/',views.create_ques,name = "create-ques"),
    path('home/<str:topic>/',views.questions,name = "subject")
    
]