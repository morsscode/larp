from django.contrib import admin
from .models import Skill, Spell, Creature, Character, CharacterSpell

# Register your models here.
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(Creature)
admin.site.register(Character)
admin.site.register(CharacterSpell)