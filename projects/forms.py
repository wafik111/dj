from django.forms import ModelForm,forms
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

class TagModelForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['tag_name', ]



class CommentModelForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

class ReportComment(ModelForm):
    class Meta:
        model = Report_comments
        fields = ['reason']

class ReportProject(ModelForm):
    class Meta:
        model = Report_projects
        fields = ['reason']


class DonateProject(ModelForm):
    class Meta:
        model = Donations
        fields = ['donation']
