from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_questions": latest_questions,
    }
    return render(request, "polls/index.html", context)

def details(request, id):
    return HttpResponse("You're looking at question %s" % id)

def results(request, id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def home(response):
    return render(response, "polls/home.html", {})