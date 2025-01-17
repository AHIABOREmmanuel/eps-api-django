from django.db import models
from django.utils import timezone


# Create your models here.

class Vehicule(models.Model):
    id = models.AutoField(primary_key=True)
    modele = models.CharField(max_length=255)
    def __str__(self):
        return self.modele

class Piece(models.Model):
    id = models.AutoField(primary_key=True)
    piece = models.CharField(max_length=255)

    def __str__(self):
        return self.piece

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


class Engin(models.Model):
    id = models.AutoField(primary_key=True)
    photo= models.ImageField(upload_to='Engin',null=False)
    marque = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=255)
    date= models.DateTimeField(default=timezone.now)
    lieu = models.CharField(max_length=255)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE,related_name='engin',default=1)
    Commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE,related_name='engin',default=1)
    Saisie = models.ForeignKey(Saisie, on_delete=models.CASCADE,related_name='engins_saisies',default=1)

    def __str__(self):
        return self.marque


class Papiers(models.Model):
    id = models.AutoField(primary_key=True)
    num_immatriculation = models.CharField(max_length=255)
    date= models.DateTimeField(default=timezone.now)
    Piece = models.ForeignKey(Piece, on_delete=models.CASCADE,related_name='papiers',default=1)
    Commissariat = models.ForeignKey(Commissariat, on_delete=models.CASCADE,related_name='papiers',default=1)
    Saisie = models.ForeignKey(Saisie, on_delete=models.CASCADE,related_name='papiers_verifies',default=1)

    def __str__(self):
        return self.num_immatriculation
    
