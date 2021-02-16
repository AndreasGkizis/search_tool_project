from django.db import models
import datetime


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class Year(models.Model):
    year_published = models.DateField(default='1000')
    convention_published = models.CharField(max_length=300)
    convention_venue = models.CharField(max_length=100)


class Paper(models.Model):
    title = models.CharField(max_length=200, unique=True)
    abstract = models.CharField(max_length=1000, unique=True)
    reviewed = models.BooleanField()
    date_added = models.DateField(default=datetime.date.today)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    papers = models.ManyToManyField(Paper)

    def __str__(self):
        return self.tag


class Material(models.Model):
    material = models.CharField(max_length=50)
    papers_id = models.ManyToManyField(Paper, through='PaperUsedMaterial')

    def __str__(self):
        return self.material


class PaperUsedMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    material_used = models.BooleanField(default=False)

    def __str__(self):
        return self.paper


class Author(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    country_of_origin = models.CharField(max_length=300)
    paper = models.ManyToManyField(Paper)

    def __str__(self):
        return "%s %s" % self.name, self.surname
