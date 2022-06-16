from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    name = models.CharField(max_length=50)

class Party(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=50)
    current_story = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class StoryMarkers(models.Model):
    pass

class PosConditions(models.Model):
    pass

class NegConditions(models.Model):
    pass

class Keyword(models.Model):
    keyword = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.keyword

class MysticKnowledge(models.Model):
    keyword = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.keyword

class Focus(models.Model):
    CHARACTER_CHOICES = [
        ('Arcanist', 'Arcanist'),
        ('AvengingMadman', 'Avenging Madman'),
        ('Exorcist', 'Exorcist'),
        ('WitchHunter', 'Witch Hunter'),
        ('Telepath', 'Telepath'),
        ('Archeologist', 'Archeologist')
    ]
    char_to_focus = models.CharField(max_length=50, choices=CHARACTER_CHOICES, default='')
    name = models.CharField(max_length=50)
    description = models.TextField()
    benefit = models.TextField()
    
    def __str__(self):
        return self.name

class Character(models.Model):
    CHARACTER_CHOICES = [
        ('Arcanist', 'Arcanist'),
        ('Avenging Madman', 'Avenging Madman'),
        ('Exorcist', 'Exorcist'),
        ('Witch Hunter', 'Witch Hunter'),
        ('Telepath', 'Telepath'),
        ('Archeologist', 'Archeologist')
    ]
    
    name = models.CharField(choices=CHARACTER_CHOICES, max_length=50)
    description = models.TextField(default='')
    vita_base = models.IntegerField(default=0)
    power_base = models.IntegerField(default=0)
    might_base = models.IntegerField(default=0)
    damage_base = models.IntegerField(default=0)
    stride_base = models.IntegerField(default=0)
    defense_base = models.IntegerField(default=0)
    archeology_base = models.IntegerField(default=0)
    awareness_base = models.IntegerField(default=0)
    ecology_base = models.IntegerField(default=0)
    faith_base = models.IntegerField(default=0)
    nerve_base = models.IntegerField(default=0)
    occult_base = models.IntegerField(default=0)
    speech_base = models.IntegerField(default=0)
    trickery_base = models.IntegerField(default=0)
    keywords = models.ManyToManyField(Keyword)
    mystic_knowledge = models.ManyToManyField(MysticKnowledge)
    special_ability = models.TextField(default='')
    focus = models.ForeignKey(Focus, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.name
    

class Hero(models.Model):
    
    name = models.CharField(max_length=50)
    character = models.OneToOneField(Character, on_delete=models.PROTECT)
    character_name = models.CharField(max_length=50, default='character')
    lore = models.IntegerField(default=0)
    coin = models.IntegerField(default=0)
    description = models.TextField(default='description')
    special_ability = models.TextField(default='special ability')
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    
    # attributes
    vita_base = models.IntegerField(default=0)
    vita_items = models.IntegerField(default=0)
    vita_mod = models.IntegerField(default=0)
    power_base = models.IntegerField(default=0)
    power_items = models.IntegerField(default=0)
    power_mod = models.IntegerField(default=0)
    might_base = models.IntegerField(default=0)
    might_items = models.IntegerField(default=0)
    might_mod = models.IntegerField(default=0)
    damage_items = models.IntegerField(default=0)
    damage_mod = models.IntegerField(default=0)
    stride_items = models.IntegerField(default=0)
    stride_mod = models.IntegerField(default=0)
    defense_items = models.IntegerField(default=0)
    defense_mod = models.IntegerField(default=0)
    damage_base = models.IntegerField(default=0)
    stride_base = models.IntegerField(default=0)
    defense_base = models.IntegerField(default=0)
    
    # skills
    archeology_items = models.IntegerField(default=0)
    archeology_mod = models.IntegerField(default=0)
    awareness_items = models.IntegerField(default=0)
    awareness_mod = models.IntegerField(default=0)
    ecology_items = models.IntegerField(default=0)
    ecology_mod = models.IntegerField(default=0)
    faith_items = models.IntegerField(default=0)
    faith_mod = models.IntegerField(default=0)
    nerve_items = models.IntegerField(default=0)
    nerve_mod = models.IntegerField(default=0)
    occult_items = models.IntegerField(default=0)
    occult_mod = models.IntegerField(default=0)
    speech_items = models.IntegerField(default=0)
    speech_mod = models.IntegerField(default=0)
    trickery_items = models.IntegerField(default=0)
    trickery_mod = models.IntegerField(default=0)
    archeology_base = models.IntegerField(default=0)
    awareness_base = models.IntegerField(default=0)
    ecology_base = models.IntegerField(default=0)
    faith_base = models.IntegerField(default=0)
    nerve_base = models.IntegerField(default=0)
    occult_base = models.IntegerField(default=0)
    speech_base = models.IntegerField(default=0)
    trickery_base = models.IntegerField(default=0)
    wanted = models.BooleanField(default=False)
    infected = models.IntegerField(default=0)
    keywords = models.TextField(blank=True)
    mystic_knowledge = models.TextField(blank=True)
    
    
    # def get_total_vita(self):
    #     return self.vita_items + self.vita_mod + self.character.vita_base
    
    # def get_total_power(self):
    #     return self.power_items + self.power_mod + self.character.power_base
    
    # def get_total_might(self):
    #     return self.might_items + self.might_mod + self.character.might_base
    
    # def get_total_damage(self):
    #     return self.damage_items + self.damage_mod + self.character.damage_base
    
    # def get_total_stride(self):
    #     return self.stride_items + self.stride_mod + self.character.stride_base
    
    # def get_total_defense(self):
    #     return self.defense_items + self.defense_mod + self.character.defense_base
    
    # def get_total_archeology(self):
    #     return self.archeology_items + self.archeology_mod + self.character.archeology_base
    
    # def get_total_awareness(self):
    #     return self.awareness_items + self.awareness_mod + self.character.awareness_base
    
    # def get_total_ecology(self):
    #     return self.ecology_items + self.ecology_mod + self.character.ecology_base
    
    # def get_total_faith(self):
    #     return self.faith_items + self.faith_mod + self.character.faith_base
    
    # def get_total_nerve(self):
    #     return self.nerve_items + self.nerve_mod + self.character.nerve_base
    
    # def get_total_occult(self):
    #     return self.occult_items + self.occult_mod + self.character.occult_base
    
    # def get_total_speech(self):
    #     return self.speech_items + self.speech_mod + self.character.speech_base
    
    # def get_total_trickery(self):
    #     return self.trickery_items + self.trickery_mod + self.character.trickery_base
    
    def __str__(self):
        return f'{self.name} the {self.character.name}'
    
    def save(self, *args, **kwargs):
       
        self.character_name = self.character.name
        self.description = self.character.description
        self.special_ability = self.character.special_ability
        self.vita_base = self.character.vita_base
        self.power_base_base = self.character.power_base
        self.might_base = self.character.might_base
        self.damage_base = self.character.damage_base
        self.stride_base = self.character.stride_base
        self.defense_base = self.character.defense_base
        self.archeology_base = self.character.archeology_base
        self.awareness_base = self.character.awareness_base
        self.ecology_base = self.character.ecology_base
        self.faith_base = self.character.faith_base
        self.nerve_base = self.character.nerve_base
        self.occult_base = self.character.occult_base
        self.speech_base = self.character.speech_base
        self.trickery_base = self.character.trickery_base
        if not self.keywords:
            for keyword in self.character.keywords.all():
                self.keywords += str(keyword) + ' '
        if not self.mystic_knowledge:
            for keyword in self.character.mystic_knowledge.all():
                self.mystic_knowledge += str(keyword) + ' '   
        
        super(Hero, self).save(*args, **kwargs)
    




    