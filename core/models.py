from django.db import models

# Create your models here.


class Profile(models.Model):
    image = models.ImageField()


class Sortable(models.Model):
    class Meta:
        abstract = True
