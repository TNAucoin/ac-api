from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=255)
    icon_path = models.URLField()
    image_path = models.URLField()
    catch_phrase = models.TextField()
    museum_phrase = models.TextField()


class CreaturePrice(models.Model):
    nook_price = models.DecimalField(max_digits=7, decimal_places=2)
    collector_price = models.DecimalField(max_digits=7, decimal_places=2)
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


class CreatureLocation(models.Model):
    LOCATION_RIVER = "R"
    LOCATION_SEA = "S"
    LOCATION_POND = "P"
    LOCATION_PIER = "D"
    LOCATION_TYPE = [
        (LOCATION_RIVER, 'River'),
        (LOCATION_SEA, 'Sea'),
        (LOCATION_POND, 'Pond'),
        (LOCATION_PIER, 'Pier')
    ]
    is_clifftop = models.BooleanField(default=False)  # river and pond locations can be limited to clifftop
    location = models.CharField(max_length=1, choices=LOCATION_TYPE, default=LOCATION_RIVER)


class CreatureRarity(models.Model):
    RARITY_COMMON = "C"
    RARITY_UNCOMMON = "U"
    RARITY_RARE = "R"
    RARITY_ULTRA_RARE = "UR"
    RARITY_TYPE = [
        (RARITY_COMMON, 'Common'),
        (RARITY_UNCOMMON, 'Uncommon'),
        (RARITY_RARE, 'Rare'),
        (RARITY_ULTRA_RARE, 'Ultra-Rare')
    ]
    rarity = models.CharField(max_length=2, choices=RARITY_TYPE, default=RARITY_TYPE)


class CreatureWeather(models.Model):
    WEATHER_ANY = 'A'
    WEATHER_PRECIPITATION = 'P'
    WEATHER_TYPE = [
        (WEATHER_ANY, 'Any'),
        (WEATHER_PRECIPITATION, 'Rain or Snow'),
    ]
    weather = models.CharField(max_length=1, choices=WEATHER_TYPE, default=WEATHER_ANY)


class CreatureAvailability(models.Model):
    available_all_day = models.BooleanField(default=False)
    available_all_year = models.BooleanField(default=False)
    months_available_northern = ArrayField(models.IntegerField())
    months_available_southern = ArrayField(models.IntegerField())
    available_time = ArrayField(models.IntegerField())
    weather = models.ForeignKey(CreatureWeather, on_delete=models.CASCADE)
    location = models.ForeignKey(CreatureLocation, on_delete=models.CASCADE)
    rarity = models.ForeignKey(CreatureRarity, on_delete=models.CASCADE)
