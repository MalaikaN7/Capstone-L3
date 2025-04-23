from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        print(selected_choice.votes)
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)


@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})