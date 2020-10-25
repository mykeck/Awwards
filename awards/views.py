from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    projects = Project.objects.all()
    return render(request,'homepage.html',{'projects': projects})


@login_required(login_url="/accounts/login/") 
def post_project(request):
    current_user = request.user   

