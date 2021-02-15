from django.contrib import admin
from search_tool_app.models import Type, Year, Papers, Materials, Tags, Language, Author

# Register your models here. Language, PaperUsedMaterial
admin.site.register(Type)
admin.site.register(Year)
admin.site.register(Language)
admin.site.register(Papers)
admin.site.register(Materials)
# admin.site.register(PaperUsedMaterial)
admin.site.register(Tags)
admin.site.register(Author)
