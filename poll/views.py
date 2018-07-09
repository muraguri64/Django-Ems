from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from poll.models import *

def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = "Polls"
    context['questions'] = questions

    return render(request, 'poll/index.html', context)

def details(request,id):
    try:
        context = {}
        question = Question.objects.get(id=id)
        context['question'] = question
    except:
        raise Http404

    return render(request, 'poll/details.html', context)

def poll(request,id):
    if request.method == 'GET':
        try:
            context = {}
            question = Question.objects.get(id=id)
            context['question'] = question
        except:
            raise Http404

        return render(request, 'poll/poll.html', context)

    elif request.method == 'POST':
        ret = Answer.objects.create(user_id=1, choice_id=request.POST['answer'])
        if ret:
            return HttpResponse('<h2>Your vote is done successfully!</h2>')
        else:
            return HttpResponse('<h2>Error Occured!</h2>')

    else:
        pass
