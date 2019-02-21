from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('base/',views.profile_info,name="Home" ),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),


]
