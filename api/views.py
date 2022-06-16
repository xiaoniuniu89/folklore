from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import HeroSerializer, PartySerializer
from .models import Party
from rest_framework.generics import ListAPIView

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api',
    ]
    return Response(routes)

@api_view(['POST', 'GET'])
def partyListCreate(request):
    
    if request.method == 'GET':
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        party = Party.objects.create(
            name=data['name']
        )
        serializer = PartySerializer(party, many=False)
        return Response(serializer.data)


