from django.forms import ModelForm
from django import forms
from .models import Question, Answer, User
from django.contrib.auth.forms import UserCreationForm

#formularz pytania
class QuesForm(ModelForm):
    class Meta:
        model = Question
        fields = ['topic','title','question']
#formularz odpowiedzi
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your answer here...'}),
        }
#formularz rejestracji
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
