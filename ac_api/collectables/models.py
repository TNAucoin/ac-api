from django.db import models


# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=255)
    icon_path = models.URLField()
    image_path = models.URLField()
    catch_phrase = models.TextField()
    museum_phrase = models.TextField()


class CreaturePrice(models.Model):
    nook_price = models.DecimalField(max_digits=7, decimal_places=2)
    flick_price = models.DecimalField(max_digits=7, decimal_places=2)
    creature = models.OneToOneField(Creature, on_delete=models.PROTECT, primary_key=True)


class CreatureCategory(models.Model):
    CREATURE_BUG = 'B'
    CREATURE_FISH = 'F'
    CREATURE_SEA = 'S'
    CREATURE_MISC = 'M'

    CREATURE_TYPE = [
        (CREATURE_BUG, 'Bug'),
        (CREATURE_FISH, 'Fish'),
        (CREATURE_SEA, 'Sea'),
        (CREATURE_MISC, 'Misc')
    ]

    type = models.CharField(max_length=1, choices=CREATURE_TYPE, default=CREATURE_MISC)
    creature = models.ForeignKey(Creature, on_delete=models.PROTECT)
