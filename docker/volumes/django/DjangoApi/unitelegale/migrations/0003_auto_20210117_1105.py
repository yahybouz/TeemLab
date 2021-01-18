# Generated by Django 3.1.5 on 2021-01-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unitelegale', '0002_auto_20210116_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitelegale',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='unitelegale',
            name='date_fin',
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='activitePrincipaleUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='anneeCategorieEntreprise',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='anneeEffectifsUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='caractereEmployeurUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='categorieEntreprise',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='categorieJuridiqueUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementActivitePrincipaleUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementCaractereEmployeurUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementCategorieJuridiqueUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementDenominationUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementDenominationUsuelleUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementEconomieSocialeSolidaireUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementNicSiegeUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementNomUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='changementNomUsageUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='dateCreationUniteLegale',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='dateDebut',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='dateDernierTraitementUniteLegale',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='dateFin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='denominationUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='denominationUsuelle1UniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='denominationUsuelle2UniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='denominationUsuelle3UniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='economieSocialeSolidaireUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='identifiantAssociationUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='nicSiegeUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='nomUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='nomUsageUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='nombrePeriodesUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='nomenclatureActivitePrincipaleUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='prenom1UniteLegale',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='prenom2UniteLegale',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='prenom3UniteLegale',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='prenom4UniteLegale',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='prenomUsuelUniteLegale',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='pseudonymeUniteLegale',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='sexeUniteLegale',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='sigleUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='statutDiffusionUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='trancheEffectifsUniteLegale',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='unitelegale',
            name='unitePurgeeUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='unitelegale',
            name='changementEtatAdministratifUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='unitelegale',
            name='etatAdministratifUniteLegale',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='unitelegale',
            name='siren',
            field=models.CharField(max_length=70, null=True),
        ),
    ]