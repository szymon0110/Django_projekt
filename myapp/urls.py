from django.urls import path 
from . import views


urlpatterns = [
    path('question/<int:qs_id>/',views.question_detail,name = "question"),
    path('',views.home, name="home"),
    path('login/',views.LoginSite, name="login"),
    path('registration/',views.SignUpSite, name='register'),
    path('logout/',views.UserLogout, name="logout"),
    path('create_question/',views.create_ques,name = "create-ques"),
    path('<str:topic>/',views.questions,name = "subject")
    
]