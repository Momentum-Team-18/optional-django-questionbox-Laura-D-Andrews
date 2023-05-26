from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question, Answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
