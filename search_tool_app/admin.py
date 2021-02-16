from django.contrib import admin
from search_tool_app.models import Type, Year, Paper, Material, Tag, Language, Author, PaperUsedMaterial

# Register your models here. Language, PaperUsedMaterial
admin.site.register(Type)
admin.site.register(Year)
admin.site.register(Language)
admin.site.register(Paper)
admin.site.register(Material)
admin.site.register(PaperUsedMaterial)
admin.site.register(Tag)
admin.site.register(Author)
