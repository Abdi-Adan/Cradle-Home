# Generated by Django 3.0.7 on 2020-07-07 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_profile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume_pdf',
        ),
    ]
