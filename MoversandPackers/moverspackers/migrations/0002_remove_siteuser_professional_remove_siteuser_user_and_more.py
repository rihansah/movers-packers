# Generated by Django 4.0.4 on 2022-05-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moverspackers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='professional',
        ),
        migrations.RemoveField(
            model_name='siteuser',
            name='user',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]