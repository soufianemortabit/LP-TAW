# Generated by Django 5.0.1 on 2024-01-24 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Afcon', '0002_equipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_int_equipe', models.IntegerField(default=1)),
                ('score_int_equipe', models.IntegerField(default=0)),
                ('id_ext_equipe', models.IntegerField(default=1)),
                ('score_ext_equipe', models.IntegerField(default=0)),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Afcon.groupes')),
            ],
        ),
    ]
