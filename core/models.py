from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Category ID')
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Country ID')
    name = models.CharField(max_length=50, verbose_name='Country Name')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Author Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country Author', null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    isbn = models.CharField(max_length=10, verbose_name='ISBN', primary_key=True)
    title = models.CharField(max_length=50, verbose_name='Title')
    year = models.DateField(verbose_name='Year Published')
    description = models.TextField(verbose_name='Description')
    category = models.ManyToManyField(Category, verbose_name='Category')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author', null=True, blank=True)

    def __str__(self):
        return self.title