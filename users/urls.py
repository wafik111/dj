from django.urls import path
from . import views

urlpatterns = [
    # path('base/',views.index ),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('home/',views.index,name='home')
]
