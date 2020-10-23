from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def homepage(request):
    projects = Project.objects.all()
    return render(request,'homepage.html',{'projects': projects})

