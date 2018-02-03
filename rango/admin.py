from django.contrib import admin  #import
from rango.models import Category, Page #import


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin) #import
admin.site.register(Page, PageAdmin) #import
