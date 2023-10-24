from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Category ID')
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name