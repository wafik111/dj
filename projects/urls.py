from django.urls import path
from .views import *
# app_name="projects"
urlpatterns = [
    path('home/',home, name="home_page"),
    path('users/',create_project , name="create_project"),
    path('rate/<int:id>',rate, name="rate"),
    path('info/<int:id>',project_info, name="info"),
    path('delete/<int:id>',remove, name="delete"),
    path('reportc/<int:id>',report_comment, name="reportc"),
    path('reportp/<int:id>',report_project, name="reportp"),
    path('donate/<int:id>',donate_project, name="donate"),

]
