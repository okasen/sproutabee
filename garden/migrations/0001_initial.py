# Generated by Django 3.1.7 on 2021-04-03 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('width', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('ALLOT', 'Allotment'), ('GARDEN', 'Garden')], default='GARDEN', max_length=6)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
