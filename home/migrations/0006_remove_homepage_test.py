# Generated by Django 2.2.16 on 2020-09-02 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='test',
        ),
    ]
