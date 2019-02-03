from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import *
from .models import *
from django.db.models import Avg
from django.forms import modelformset_factory


def index(request):
    f= Projects.objects.all()
    return render(request,'projects/projects.html',{'key':f,'t':rate})

def show_users(request):
    members= Users.objects.all()
    return render(request,'projects/users.html',{'members':members})


def remove(request,id):
    Projects.objects.get(id=id).delete()
    return redirect(index)


###########################################################################################
def info(request,id):
    selected_project= Projects.objects.get(id=id)
    if request.method == 'POST':
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = get_object_or_404(Users, pk=2)  # will be replaced with session user
            comment.project = selected_project
            comment.save()
            return HttpResponseRedirect(reverse('info', args=[selected_project.id]))
    else:
        pics = selected_project.project_images_set.all
        rate = selected_project.rates_set.all().aggregate(Avg('rate'))
        comment_form = CommentModelForm()
        comments= selected_project.comments_set.all()
        context = {'project': selected_project, 'rate': rate['rate__avg'],
                   'form': comment_form ,'comments' : comments,'pic' : pics}
        return render(request, 'projects/project_info.html', context)

    ##################################################################################

def create_project(request,id):
    project_owner= get_object_or_404(Users,pk=id)
    PicFormset = modelformset_factory(Project_images, fields=('project_img',), extra=4)

    if request.method == 'POST':
        # populate the form with the data
        form = ProjectForm(request.POST)
        formset = PicFormset(request.POST,request.FILES)


        if form.is_valid() and formset.is_valid():
            print('entered if ')
            projects=form.save(commit=False)
            projects.owner = project_owner
            projects.save()
            # tags_str = request.POST['tag_name'].split(',')
            # for tag in tags_str:
            #     tag = Tags(tag_name=tag)
            #     tag.save()
            #     projects.tag.add(tag)
            for pic in formset:


                # picture = Project_images(project_img=pic.cleaned_data['project_img'], project=projects)

                # picture.save()


            return HttpResponseRedirect(reverse('Home'))
    else:
        form = ProjectForm()
        formset = PicFormset(queryset=Project_images.objects.none())
        context = {
            'form': form,
            'project_owner': project_owner,
            'formset': formset,
        }

    return render(request, 'projects/index.html', context)

    # # if request GET create empty form
    # else:
    #     form = ProjectForm()
    #     form2 = project_img()
    #     context={
    #         'form':form,
    #         'form2':form2,
    #         'owner':project_owner,
    #     }
    # return render(request,'projects/index.html',context)

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

