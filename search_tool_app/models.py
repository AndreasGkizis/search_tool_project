from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=100)


class Year(models.Model):
    year_published = models.DateField()
    convention_published = models.CharField(max_length=300)
    convention_venue = models.CharField(max_length=100)


class Papers(models.Model):
    title = models.CharField(max_length=200, unique=True)
    abstract = models.CharField(max_length=1000, unique=True)
    reviewed = models.BooleanField(default=False)
    date_added = models.DateField()
    year_id = models.ForeignKey(Year)  # on_delete = ?
    type_id = models.ForeignKey(Type)


class Tags(models.Model):
    tag = models.CharField(max_length=50)
    papers = models.ManyToManyField(Papers)


class Author(models.Model):
    name = models.CharField()
    surname = models.CharField()
    country_of_origin = models.CharField()
    paper = models.ManyToManyField(Papers)

class Materials(models.Model):




