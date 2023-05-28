from django import forms
from .models import Question, Answer, User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_title', 'question_text', 'user', 'published_time')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_text', 'answer_time')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
