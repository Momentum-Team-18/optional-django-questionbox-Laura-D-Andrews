from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


# Create your views here.


def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'project/list_questions.html', {'questions': questions})


def ask_question(request):
    if request.method == "GET":
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        form.save()
        return redirect('list-questions')
    return render(request, 'project/ask_question.html', {'form': form})


def question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'project/question_details.html', {'question': question})


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


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect("list-questions")


def answer_question(request, pk):
    if request.method == "GET":
        form = AnswerForm()
    else:
        form = AnswerForm(request.POST)
        form.save()
        return redirect('question-details')
    return render(request, 'project/answer_question.html', {'form': form})


def edit_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.method == "GET":
        form = AnswerForm(instance=answer)
    else:
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('question-details')
    return render(request, 'project/edit_answer.html', {'form': form})



