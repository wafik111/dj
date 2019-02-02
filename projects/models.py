from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    facebook = models.URLField(blank=True)
    profile_img = models.ImageField(upload_to="imag_up/", default="imag_up/none/n0.jpg")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    ##########################################

class Projects(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    category_options = (('so', 'social'),
                        ('sp', 'sport'),
                        )
    category = models.CharField(max_length=2, choices=category_options,
                                default='social',
                                )
    target_money = models.PositiveIntegerField(null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#################################################################

class Project_images(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    project_img = models.ImageField(upload_to="imag_up/", default="imag_up/none/n0.jpg")

class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Rates(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
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
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    donation = models.PositiveIntegerField(default=0)

class Report_comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    reason = models.TextField(default='default')

class Report_projects(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    reason = models.TextField(default='default')

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    project = models.ManyToManyField(Projects)

# Create your models here.
