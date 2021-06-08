from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import datetime


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return str(self.language)


class Year(models.Model):
    year_published = models.DateField(default='1000')
    convention_published = models.CharField(max_length=300)
    convention_venue = models.CharField(max_length=100)

    def __str__(self):
        return str(self.year_published.year)


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tag)


class Material(models.Model):
    material = models.CharField(max_length=50)

    def __str__(self):
        return str(self.material)


class Paper(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    slug = models.SlugField(default="no-slug")
    pdf = models.FileField(upload_to="papers/pdfs", null=True)
    abstract = models.TextField(max_length=1000, unique=True, null=True)
    reviewed = models.BooleanField(default=False)
    date_added = models.DateField(default=datetime.date.today, null=True)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    language = models.ManyToManyField(Language)
    tag = models.ManyToManyField(Tag)
    material = models.ManyToManyField(Material, through='PaperUsedMaterial')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Paper, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('show_publication', kwargs={'slug': self.slug})

    # def delete(self, using=None, keep_parents=False):

    def __str__(self):
        return str(self.title)


class PaperUsedMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    material_used = models.BooleanField(default=False)

    def __str__(self):
        return str(self.paper)


class Author(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    country_of_origin = models.CharField(max_length=300)
    paper = models.ManyToManyField(Paper, blank=True)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)
