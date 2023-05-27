from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30, unique=True)
    email = models.EmailField(('email address'), unique=True)

    def __str__(self):
        return self.email


class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_text = models.TextField()
    published_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    answer_title = models.CharField(max_length=200)
    answer_text = models.TextField()
    answer_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return self.answer_title
