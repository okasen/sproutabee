# Generated by Django 3.1.7 on 2021-04-05 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0003_auto_20210405_2138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GardenStucture',
            new_name='GardenStructure',
        ),
        migrations.AddField(
            model_name='garden',
            name='structures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='garden.gardenstructure'),
        ),
    ]
