from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=12,validators = [ RegexValidator(regex='^01[0|1|2|5][0-9]{8}$',message='Phone must be start 010, 011, 012, 015 and all number contains 11 digits',code='invalid number') ])
   
    birthdate = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=100, blank=True)
    facebook = models.URLField(blank=True)
    profile_img = models.ImageField(upload_to="imag_up/", default="imag_up/none/n0.jpg")

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
