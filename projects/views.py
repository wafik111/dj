from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import *
from .models import *
from django.db.models import Avg
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required


# @login_required()
def home(request):
    f= Projects.objects.all()
    rate_p = Rates.objects.all()
    return render(request,'projects/projects.html',{'key':f,'rate':rate_p})



@login_required()
def remove(request,id):
    Projects.objects.get(id=id).delete()
    return redirect(home)


# @login_required()


###########################################################################################
@login_required()
def project_info(request,id):
    selected_project= Projects.objects.get(id=id)
    if request.method == 'POST':
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user.profile  # will be replaced with session user
            comment.project = selected_project
            comment.save()
            return HttpResponseRedirect(reverse('info', args=[selected_project.id]))
    else:
        pics = selected_project.project_images_set.all
        rate = selected_project.rates_set.all().aggregate(Avg('rate'))
        comment_form = CommentModelForm()
        comments= selected_project.comments_set.all()
        # tags = selected_project.tags_set.all()
        context = {'project': selected_project, 'rate': rate['rate__avg'],
                   'form': comment_form ,'comments' : comments,'pic' : pics,}
        return render(request, 'projects/project_info.html', context)

    ############
@login_required()
def create_project(request,):

    PicFormset = modelformset_factory(Project_images, fields=('project_img',), extra=4)

    if request.method == 'POST':
        # populate the form with the data
        form = ProjectForm(request.POST)
        formset = PicFormset(request.POST,request.FILES)
        if form.is_valid() and formset.is_valid():
            projects=form.save(commit=False)
            projects.owner = request.user.profile
            projects.save()
            tags_str = request.POST['tag'].split(',')
            for tag in tags_str:
                tag = Tags(tag_name=tag)
                tag.save()
                projects.tag.add(tag)
            for pic in formset:
                try:
                    picture = Project_images(project_img=pic.cleaned_data['project_img'], project=projects)
                    picture.save()
                except Exception as e:
                    break
            return HttpResponseRedirect(reverse('home_page'))
    else:
        form = ProjectForm()
        formset = PicFormset(queryset=Project_images.objects.none())
        context = {
            'form': form,
            'formset': formset,
        }

    return render(request, 'projects/index.html', context)


@login_required()
def rate(request,id):
    selected_project = get_object_or_404(Projects,pk=id)
    # owner_id = selected_project.owner.id
    # owner = get_object_or_404(Profile,pk=owner_id)
    if request.method == 'POST':
        form = Rate_project(request.POST)

        if form.is_valid():
            Rates=form.save(commit=False)
            Rates.user = request.user.profile
            Rates.project = selected_project
            Rates.save()
            return HttpResponseRedirect(reverse('home_page'))
        # if the request with GET or any other method create empty form
    else:
        form = Rate_project()
        context = {
            'form':form,
            'project':selected_project,
        }
    return render(request,'projects/rate.html',context)
@login_required()
def report_comment(request,id):
    reported_comment = Comments.objects.get(id=id)

    if request.method == 'POST':
        form = ReportComment(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user.profile
            report.comment = reported_comment
            report.save()
            return HttpResponse('thank you for contacting us ',)
    else:
        form = ReportComment()
        context = {'form':form}
        return render(request,'projects/reportc.html',context)

@login_required()
def report_project(request,id):
    reported_project = Projects.objects.get(id=id)
    if request.method == 'POST':
        form = ReportProject(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user.profile
            report.project = reported_project
            report.save()
            return HttpResponse('thank you for contacting us ', )
    else:
        form = ReportProject()
        context = {'form':form}
        return render(request, 'projects/reportc.html', context)

@login_required()
def donate_project(request,id):
    donated_project = Projects.objects.get(id=id)
    if request.method == 'POST':
        form = DonateProject(request.POST)
        if form.is_valid():
            donate = form.save(commit=False)
            donate.user = request.user.profile
            donate.project = donated_project
            donate.save()
            return HttpResponse(' thank you for your donation  ', )
    else:
        form = DonateProject()
        context = {'form':form}
        return render(request, 'projects/donate.html', context)








