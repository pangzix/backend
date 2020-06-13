from django.contrib import admin
from .models import ArticlePost,Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','created','updated','category','author','top']
    # fields = ['title']

admin.site.register(ArticlePost,ArticleAdmin)
admin.site.register(Category)

