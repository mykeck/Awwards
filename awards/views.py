from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, PostProjectForm
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    projects = Project.objects.all()
    return render(request,'homepage.html',{'projects': projects})

def search_results(request):
    if 'title' in request.GET and request.GET['title']:
        searched_term = request.GET.get('title')
        titles = project.objects.filter(title_icontains= searched_term)
        message = f"{searched_term}"
        return render(request,'search.html',{'message':message,'titles':titles})

    else:
        message = "you haven't searched for any term"
        return render(request,'search.html',{'message':message}) 

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    return render(request, 'profile.html', {"profile" : profile} )           



@login_required(login_url="/accounts/login/") 
def post_project(request):
    current_user = request.user 

    if request.method == "POST":
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user
            project.save()
        return redirect('homepage')
    else:
        form = PostProjectForm()
    return render(request, 'post_project.html', {"form": form})  

