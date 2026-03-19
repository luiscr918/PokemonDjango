from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Pokemon(models.Model):
    pokedex_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    # cardinalidad:
    types = models.ManyToManyField(Type, related_name="pokemons")

    def __str__(self):
        return str(self.name)
