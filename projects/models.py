from django.db import models
from users.models import *
from django.db.models import Avg

    ##########################################
class Tags(models.Model):
    tag_name = models.CharField(max_length=50)


    def __str__(self):
        return self.tag_name
#################################################
class Projects(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    category_options = (('so', 'social'),
                        ('sp', 'sport'),
                        ('he','health'),
                        ('ch','charity')
                        )
    category = models.CharField(max_length=2, choices=category_options,
                                default='social',
                                )
    target_money = models.PositiveIntegerField(null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)


    def __str__(self):
        return self.title
    def first_image(self):
        return self.project_images_set.all()[:1]
    def project_rate(self):
        rate = self.rates_set.all().aggregate(Avg('rate'))
        t = rate['rate__avg']
        return t
    def project_donaters(self):
        return self.donations_set.all()

    def donation_check(self):
        total=0
        for donate in self.donations_set.all():
            total+= donate.donation
        return total < (self.target_money/4)
    
    def donation_percent(self):
        total=0
        for donate in self.donations_set.all():
            total+= donate.donation
        return int((total/self.target_money)*100)




#################################################################


class Project_images(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    project_img = models.ImageField(upload_to="imag_up/", default="imag_up/none/n0.jpg")

class Comments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Rates(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    rate_options=(
        ('1',1),('2',2),('3',3),
        ('4',4),('5',5),
    )
    rate = models.CharField(max_length=1, choices=rate_options,
                                default='5',
                                )

    def __str__(self):
        return '%s'% (self.project)

class Donations(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    donation = models.PositiveIntegerField(blank=False)

class Report_comments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    reason = models.TextField(default='default')
    def __str__(self):
        return self.reason

class Report_projects(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    reason = models.TextField(default='default')
    def __str__(self):
        return self.reason



# Create your models here.
