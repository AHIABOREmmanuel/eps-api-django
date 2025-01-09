from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from backend.models import *
from api.serializers import *

# Create your views here.

class  MotoViewSet(viewsets.ModelViewSet):

    queryset = Moto.objects.all()
    serializer_class = MotoSerializer



class  SaisieViewSet(viewsets.ModelViewSet):

    queryset = Saisie.objects.all()
    serializer_class = SaisieSerializer 



class  PapiersViewSet(viewsets.ModelViewSet):

    queryset = Papiers.objects.all()
    serializer_class = PapiersSerializer 


class  CommissariatViewSet(viewsets.ModelViewSet):

    queryset = Commissariat.objects.all()
    serializer_class = CommissariatSerializer
    

class  Agent_PoliceViewSet(viewsets.ModelViewSet):

    queryset = Agent_Police.objects.all()
    serializer_class = Agent_PoliceSerializer 