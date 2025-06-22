from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=30)

def __repr__(self):
    return f"Color:{self.name}({self.id})"
# Create your models here.
class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(default='Описание по умолчанию')
    colors = models.ManyToManyField(to=Color)
    def __repr__(self):
        return f" Item name:{self.name} brand:{self.brand}"