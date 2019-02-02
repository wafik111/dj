from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title','body','category',
                  'target_money','start_date',
                  'end_date',
                  ]

class Rate_project(ModelForm):
    class Meta:
        model = Rates
        fields = ['rate']

class project_img(ModelForm):
    class Meta:
        model = Project_images
        fields = ['project_img']


