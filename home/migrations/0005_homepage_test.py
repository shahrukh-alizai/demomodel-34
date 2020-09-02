# Generated by Django 2.2.16 on 2020-09-02 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_demo"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="test",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_test",
                to="home.Demo",
            ),
        ),
    ]
