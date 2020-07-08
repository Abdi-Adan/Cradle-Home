# Generated by Django 3.0.7 on 2020-07-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_contactme_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contactme',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactme',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
