from rest_framework import serializers
from api.models import *


class VehiculeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'


class PieceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'


class EnginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Engin
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


