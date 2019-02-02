from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(Project_images)
admin.site.register(Comments)
admin.site.register(Rates)
admin.site.register(Donations)
admin.site.register(Report_comments)
admin.site.register(Report_projects)
admin.site.register(Tags)

# Register your models here.
