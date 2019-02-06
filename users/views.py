from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from projects.models import *
from django.contrib.auth import ( authenticate,login,logout, get_user_model)
from django.contrib.auth.decorators import login_required

def index(request):
    data = Profile.objects.get(id=2)
    data_projects =Projects.objects.get(owner=data.user)
    # data_projects =Projects.objects.get(id=data.auther_name_id)
    details={
        'names':data.user,
        # 'lname':data.user,
        'phone':data.phone,
        # 'email':data.email,
        # 'password':data.password,
        'country':data.country,
        'BD':data.birthdate,
        # 'facebook':data.facebook,
        'project': data_projects
     }
    print(details)
    return render(request, 'users/profile.html',details)

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
            return redirect(login_user)
    else:

        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'users/register.html', { 'user_form': user_form,
        'profile_form': profile_form
    })
def login_user(request):

    form = signup(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        users = User.objects.get(username=username)
        user_profile= users.objects.Profile_set.all()
        # print('ccccccccccccccccccccc',user_profile)
        return render(request,"users/home.html",{'username':users,"profile":user_profile
    
    
    })    
        
    return render(request,"users/login.html",{"form":form})
# def index(request):
#     return HttpResponse('hello')

    
    

