from django.contrib import admin
from .models import Question, subject, Answer
# Register your models here.
admin.site.register(Question)
admin.site.register(subject)
admin.site.register(Answer)