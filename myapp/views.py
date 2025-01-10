from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Question, subject
from .forms import AnswerForm, QuesForm, RegistrationForm
from .forms import RegistrationForm

#strona głowna
def home(req):
    data = subject.objects.all()
    return render(req,'home.html',{'topics':data})

#lista pytań
def questions(req,topic):
    c_topic = get_object_or_404(subject, name = topic)
    qs = c_topic.questions.all()
    if not qs:
        return HttpResponse('<h1>No questions in this Topic yet<h1>')
    else:
        return render(req,'questions.html',{'questions': qs, 'subject':c_topic})

#tworzenie pytania
@login_required(login_url='login')
def create_ques(req):
    form = QuesForm()
    if req.method == 'POST':
        form = QuesForm(req.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = req.user
            question.save()
            return redirect('home')
    return render(req,'create_ques.html',{'form':form})

#logowanie użytkownika
def LoginSite(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req,username=username,password=password)
        
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,'Invalid username or password!')

    return render(req,'Login.html')
#wylogowanie użytkownika
def UserLogout(req):
    logout(req)
    return redirect('home')

#rejestracja nowego użytkownika
def SignUpSite(req):
    form = RegistrationForm()
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(req,user)
            return redirect('home')
    return render(req,'Register.html', {'form':form})

#system odpowiadania na pytania
@login_required(login_url='login')
def question_detail(request, qs_id):
    question = get_object_or_404(Question, id=qs_id)
    answers = question.answers.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question', qs_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'form': form})
