from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

#model przedmiotuu
class subject(models.Model):
    name = models.CharField(max_length=150,null=False)
    def __str__(self):
        return str(self.name)

#model pytania
class Question(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,null=True)  
    topic = models.ForeignKey(subject, related_name='questions',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120,null=False,default="Tytuł pytania")
    question = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    class Meta():
        ordering = ['-created']

    def __str__(self):
        return self.title
#model odpowiedzi
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content