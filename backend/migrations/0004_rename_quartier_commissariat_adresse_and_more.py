# Generated by Django 5.1.3 on 2025-01-08 07:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_saisie_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commissariat',
            old_name='quartier',
            new_name='adresse',
        ),
        migrations.RemoveField(
            model_name='commissariat',
            name='images',
        ),
        migrations.AddField(
            model_name='agent_police',
            name='matricule',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='commissariat',
            name='tel',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='saisie',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='agent_police',
            name='telephone',
            field=models.IntegerField(default=1),
        ),
    ]
