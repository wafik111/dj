from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import ( authenticate,login,logout, get_user_model)
from django.contrib.auth.decorators import login_required



def register(request):
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            t=user_form.save(commit=False)
            username = user_form.cleaned_data.get('username')
            t.save()
            profile = profile_form.save(commit=False)
            current_user = User.objects.get(username=username)
            profile.user = current_user
            profile.save()
            return redirect(profile_info)
    else:

        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'users/register.html', { 'user_form': user_form,
        'profile_form': profile_form
    })


@login_required()
def profile_info(request):
    project = request.user.profile.projects_set.all()
    context = { 'projects': project}
    return render(request, "profile.html", context)


@login_required
def profile(request):
    if request.method=='POST':
        u_form = userUpdate(request.POST,instance=request.user)
        p_from = updateProfile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid and p_from.is_valid :
            u_form.save()
            p_from.save()
            messages.successful(request,f'Done Updated')
            return redirect('home.html')
    else:
        u_form = userUpdate(instance=request.user)
        p_from = updateProfile(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form}
    return render(request,'users/home.html',context)