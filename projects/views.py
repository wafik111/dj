from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import *
from .models import *


def index(request):
    f= Projects.objects.all()
    return render(request,'projects/projects.html',{'key':f})

def show_users(request):
    members= Users.objects.all()
    return render(request,'projects/users.html',{'members':members})

def create_project(request,id):
    project_owner= get_object_or_404(Users,pk=id)

    if request.method == 'POST':
        # populate the form with the data
        form = ProjectForm(request.POST)
        form2 = project_img(request.POST)

        if form.is_valid():
            Projects=form.save(commit=False)
            images = form.save(commit=False)
            images.project = 1
            Projects.owner = project_owner
            # print(project_owner.)
            Projects.save()
            images.save()
            return HttpResponseRedirect(reverse('Home'))
    # if request GET create empty form
    else:
        form = ProjectForm()
        form2 = project_img()
        context={
            'form':form,
            'form2':form2,
            'owner':project_owner,
        }
    return render(request,'projects/index.html',context)

def rate(request,id):
    selected_project = get_object_or_404(Projects,pk=id)
    owner_id = selected_project.owner.id
    owner = get_object_or_404(Users,pk=owner_id)
    if request.method == 'POST':
        print('post')
        form = Rate_project(request.POST)

        if form.is_valid():
            Rates=form.save(commit=False)
            Rates.user = owner
            Rates.project = selected_project
            Rates.save()
            print('saved')
            return HttpResponseRedirect(reverse('Home'))
        # if the request with GET or any other method create empty form
    else:
        print('else')
        form = Rate_project()

        context = {
            'form':form,
            'user':owner,
            'project':selected_project
        }
    return render(request,'projects/rate.html',context)

