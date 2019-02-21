from django.contrib import admin
from . import models 

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Article,ArticleAdmin)