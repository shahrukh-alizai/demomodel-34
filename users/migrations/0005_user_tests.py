# Generated by Django 2.2.16 on 2020-09-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_user_std"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tests",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
