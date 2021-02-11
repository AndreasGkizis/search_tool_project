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
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE)  # on_delete = ?
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)


class Tags(models.Model):
    tag = models.CharField(max_length=50)
    papers = models.ManyToManyField(Papers)


class Author(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    country_of_origin = models.CharField(max_length=300)
    paper = models.ManyToManyField(Papers)

#  not sure how to do that


class PaperUsedMaterial(models.Model):
    pass
# ???? why ????


class Materials(models.Model):
    material = models.CharField(max_length=50)
    papers_id = models.ForeignKey(PaperUsedMaterial, on_delete=models.CASCADE)


class Language(models.Model):
    language = models.CharField(max_length=100, null=False)


# class PaperUsedMaterial(models.Model):
#     paper_used_material_id = models.UUIDField
#     material = models.ForeignKey(Materials, on_delete=models.CASCADE)
#     paper = models.ForeignKey(Papers, on_delete=models.CASCADE)
#     material_used = models.BooleanField()