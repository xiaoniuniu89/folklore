from rest_framework.serializers import ModelSerializer
from .models import Hero, Party

class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'character', 'party']

class PartySerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'
