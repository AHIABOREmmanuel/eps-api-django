from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from backend.models import *
from api.serializers import *
from backend.models import*
import urllib.parse


# Create your views here.




class VehiculeViewSet(viewsets.ModelViewSet):

    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer


class PieceViewSet(viewsets.ModelViewSet):

    queryset = Piece.objects.all()
    serializer_class = PieceSerializer


class EnginViewSet(viewsets.ModelViewSet):

    queryset = Engin.objects.all()
    serializer_class = EnginSerializer


class  SaisieViewSet(viewsets.ModelViewSet):

    queryset = Saisie.objects.all()
    serializer_class = SaisieSerializer 



class  PapiersViewSet(viewsets.ModelViewSet):

    queryset = Papiers.objects.all()
    serializer_class = PapiersSerializer 


class  CommissariatViewSet(viewsets.ModelViewSet):

    queryset = Commissariat.objects.all()
    serializer_class = CommissariatSerializer
     


def get_queryset(self):
    queryset = Engin.objects.all()
    immatriculation = self.request.query_params.get('immatriculation', None)
    if immatriculation:
        immatriculation = urllib.parse.unquote(immatriculation)  
        queryset = queryset.filter(immatriculation__icontains=immatriculation)
    return queryset

