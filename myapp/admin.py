from django.contrib import admin
from .models import Question, subject, Answer
# Rejestracja modeli w bazie danych
admin.site.register(Question)
admin.site.register(subject)
admin.site.register(Answer)