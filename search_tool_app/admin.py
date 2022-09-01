from django.contrib import admin
from .models import (PaperUsedMaterial, Type, Year, Paper, Material, Tag,
                     Language, Author)


class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'reviewed', 'type_id')


class PaperUsedMaterialAdmin(admin.ModelAdmin):
    list_display = ('paper', 'material', 'material_used',)


# Register your models here. Language, PaperUsedMaterial
admin.site.register(Type)
admin.site.register(Year)
admin.site.register(Language)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Material)
admin.site.register(PaperUsedMaterial, PaperUsedMaterialAdmin)
admin.site.register(Tag)
admin.site.register(Author)
