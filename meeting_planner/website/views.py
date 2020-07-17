from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()) + " by Ulrich Von Lichtenstein")

def about(request):
    return HttpResponse("<b><p> Steezus is the creator and founder of Freedom Coders .org \n </p></b>"
                        "<p>founded in 2020, ABC.\n </p>"
                        "OneMoreLine")

