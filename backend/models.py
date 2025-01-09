from django.db import models
from django.utils import timezone


# Create your models here.
class Saisie(models.Model):
    id = models.AutoField(primary_key=True)
    motif = models.TextField()
    def __str__(self):
        return self.motif



class Commissariat(models.Model):
    id = models.AutoField(primary_key=True)
    arrondissement = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    tel = models.IntegerField(default=1)
    def __str__(self):
        return self.arrondissement


class Agent_Police(models.Model):
    id = models.AutoField(primary_key=True)
    nom= models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    matricule= models.CharField(max_length=255,default=1)
    telephone = models.IntegerField(default=1)

    def __str__(self):
        return self.matricule

class Moto(models.Model):
    id = models.AutoField(primary_key=True)
    photo= models.ImageField(upload_to='Moto',null=False)
    marque = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=255)
    date= models.DateTimeField(default=timezone.now)
    agent_police = models.ForeignKey(Agent_Police, on_delete=models.CASCADE,related_name='motos_principaux',default=1)
    Commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE,related_name='motos',default=1)
    Saisie = models.ForeignKey(Saisie, on_delete=models.CASCADE,related_name='motos_saisies',default=1)

    def __str__(self):
        return self.marque


class Papiers(models.Model):
    id = models.AutoField(primary_key=True)
    libellé = models.CharField(max_length=255)
    noms = models.CharField(max_length=255)
    num_identification = models.CharField(max_length=255)
    date= models.DateTimeField(default=timezone.now)
    agent_police = models.ForeignKey(Agent_Police, on_delete=models.CASCADE,related_name='papiers_emis',default=1)
    Commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE,related_name='papiers',default=1)
    Saisie = models.ForeignKey(Saisie, on_delete=models.CASCADE,related_name='papiers_verifies',default=1)

    def __str__(self):
        return self.noms