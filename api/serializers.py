from rest_framework import serializers
from api.models import *


class MotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'
       


class SaisieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saisie
        fields = '__all__'


class PapiersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Papiers
        fields = '__all__'


class CommissariatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commissariat
        fields = '__all__'


class Agent_PoliceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent_Police
        fields = '__all__'