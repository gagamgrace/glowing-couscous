from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from time import gmtime, strftime

def clockit(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'dee/time.html', context)
