from django.db import models
from django.core.validators import MinLengthValidator

class Creature(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Creature must be greater than 1 character")]
    )
    details = models.TextField(default="")
    #moredetails = models.CharField()

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
    #   level = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Character(models.Model):
    playerName = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Name must be greater than 1 character")]
    )
    CharacterName = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Name must be greater than 1 character")]
    )
    virtue = models.IntegerField(default=50)
    rep = models.IntegerField(default=50)
    xp = models.IntegerField(default=0)
    creatureType = models.ForeignKey(Creature, null=True, on_delete=models.SET_NULL)
    spells = models.ManyToManyField(Spell, through='CharacterSpell', verbose_name="list of spells")
    skills = models.ManyToManyField(Skill, through='CharacterSkill', verbose_name="list of skills")

    def __str__(self):
        return self.playerName


class CharacterSpell(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)


class CharacterSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
