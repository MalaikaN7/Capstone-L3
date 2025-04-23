from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    Display a list of all poll questions.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered index page with all questions.
    :rtype: HttpResponse
    """
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


@login_required
def detail(request, question_id):
    """
    Display the details and choices for a specific question.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param question_id: The ID of the question to display.
    :type question_id: int
    :return: Rendered detail page for the question.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    Handle voting for a specific choice in a question.

    :param request: The HTTP request object (must be POST).
    :type request: HttpRequest
    :param question_id: The ID of the question being voted on.
    :type question_id: int
    :return: Redirect to the results page if successful, or re-render the detail page with an error.
    :rtype: HttpResponse
    """
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
    """
    Display the results of a specific poll question.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param question_id: The ID of the question to show results for.
    :type question_id: int
    :return: Rendered results page showing vote counts.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
