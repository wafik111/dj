# Generated by Django 2.1.5 on 2019-02-08 13:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='invalid number', message='Phone must be start 010, 011, 012, 015 and all number contains 11 digits', regex='^01[0|1|2|5][0-9]{8}$')])),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True)),
                ('profile_img', models.ImageField(default='imag_up/none/n0.jpg', upload_to='imag_up/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
