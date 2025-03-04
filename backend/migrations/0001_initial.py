# Generated by Django 5.1.3 on 2025-01-10 14:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commissariat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arrondissement', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('tel', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('piece', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Saisie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('motif', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modele', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Papiers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('num_immatriculation', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Commissariat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='papiers', to='backend.commissariat')),
                ('Piece', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='papiers', to='backend.piece')),
                ('Saisie', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='papiers_verifies', to='backend.saisie')),
            ],
        ),
        migrations.CreateModel(
            name='Engin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='Engin')),
                ('marque', models.CharField(max_length=255)),
                ('immatriculation', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lieu', models.CharField(max_length=255)),
                ('Commissariat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='engin', to='backend.commissariat')),
                ('Saisie', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='engins_saisies', to='backend.saisie')),
                ('vehicule', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='engin', to='backend.vehicule')),
            ],
        ),
    ]
