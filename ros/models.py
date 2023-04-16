from django.db import models
from django.core.validators import MinLengthValidator

class Creature(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Creature must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Skill must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "spell must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Character(models.Model):
    playerName = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Skill must be greater than 1 character")]
    )
    CharacterName = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Skill must be greater than 1 character")]
    )
    virtue = models.IntegerField(default=50)
    rep = models.IntegerField(default=50)
    xp = models.IntegerField(default=0)
    creatureType = models.ForeignKey(Creature, on_delete=models.CASCADE)

    def __str__(self):
        return self.PlayerName
