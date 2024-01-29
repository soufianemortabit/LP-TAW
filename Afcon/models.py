from django.db import models

# Create your models here.
class Groupes(models.Model):
    name = models.CharField(max_length=1)

class Equipes(models.Model):
    name = models.CharField(max_length=200)
    classement = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    groupe = models.ForeignKey(Groupes, on_delete=models.CASCADE)

class Matches(models.Model):
    id_int_equipe = models.IntegerField(default=1)
    score_int_equipe = models.IntegerField(default=0)
    id_ext_equipe = models.IntegerField(default=1)
    score_ext_equipe = models.IntegerField(default=0)
    groupe = models.ForeignKey(Groupes, on_delete=models.CASCADE)