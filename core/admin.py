from django.contrib import admin
from .models import Category, Country, Author, Book


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id')

class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('id')

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Country)
