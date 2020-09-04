from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    demo = models.BigIntegerField(
        null=True,
        blank=True,
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Demo(models.Model):
    "Generated Model"
    app = models.BigIntegerField()


class Test(models.Model):
    "Generated Model"
    tests = models.BigIntegerField()


class Student(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Cars(models.Model):
    "Generated Model"
    handle = models.CharField(
        max_length=256,
    )
