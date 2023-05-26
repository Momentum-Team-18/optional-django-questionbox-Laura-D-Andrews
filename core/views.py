from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm
from .models import Question


# Create your views here.


def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'project/list_questions.html', {'questions': questions})


def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "GET":
        form = QuestionForm(instance=question)
    else:
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question-details')
    return render(request, 'project/edit_question.html', {'form': form})
