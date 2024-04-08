from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    
    context = {
        "latest_question_list" : latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist: 
    #     raise Http404("Question Does Not Exists")
    # return render(request, "polls/details.html",{"question":question})
    question = get_object_or_404(Question , pk = question_id)
    return render(request, "polls/details.html",{"question":question})
     
    

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)