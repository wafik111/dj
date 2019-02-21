from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from projects.models import *
from django.contrib.auth import ( authenticate,login,logout, get_user_model)
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response
from django.template import RequestContext


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            profile = profile_form.save(commit=False)
            user.is_active = False
            profile.user = user
            user.save()
            profile.save()
            #######CONFIRMATION##########
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })  


            mail_subject = 'Activate your KickPro account.'
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            ######################################
        


    else:

        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'users/register.html', { 'user_form': user_form,
        'profile_form': profile_form, 'registered':registered
    })

######Activation Function#################
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist()):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # profile.save()
        # registered = True
        login(request, user)
        
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        # return redirect('home')
    else:
        return HttpResponse('Activation link is invalid or Expired!')


@login_required()
def profile_info(request):
    project = request.user.profile.projects_set.all()
    context = { 'projects': project}
    return render(request, "profile.html", context)



