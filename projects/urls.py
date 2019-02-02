from django.urls import path
from .views import *
# app_name="projects"
urlpatterns = [
    path('', index , name="Home"),
    path('users/',show_users, name="show_users"),
    path('save/<int:id>',create_project , name="create_project"),
    path('rate/<int:id>',rate, name="rate"),

]
