from django.db.models import Sum, Count
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from Afcon.models import Groupes, Equipes, Matches


# Create your views here.
def index(request):
    return HttpResponse("Bonjour, bienvenue au Coupe d'Afrique des nations de football !")


def ViewAccueil(request):
    titre = "Coupe d'Afrique des nations de football"
    annee = 2023
    lieu = "cote d'ivoire"
    template = loader.get_template('Afcon/accueil.html')
    context = {'titre': titre, 'lieu': lieu, 'annee': annee}
    return HttpResponse(template.render(context, request))


def ViewGroupe(request):
    template = loader.get_template('Afcon/groupe.html')
    allGroupesSorted = getAllGroupesSorted()
    context = {'allGroupesSorted': allGroupesSorted}
    return HttpResponse(template.render(context, request))


def getAllGroupesSorted():
    allGroupesSorted = []
    for i in range(1, 7):
        allGroupesSorted.append(sorted(Equipes.objects.filter(groupe_id=i), key=lambda x: x.points, reverse=True))
    return allGroupesSorted


def ViewModifier(request, equipe_id):
    template = loader.get_template('Afcon/modifier.html')
    equipe = Equipes.objects.get(id=equipe_id)
    context = {'equipe': equipe}
    return HttpResponse(template.render(context, request))


def editPoints(request, equipe_id):
    if request.method == 'POST':
        Equipes.objects.filter(id=equipe_id).update(points=request.POST['points'])
        return redirect('../../Afcon/groupe.html', equipe_id)


def ViewMatches(request, groupe_id):
    template = loader.get_template('Afcon/matche.html')
    equipes = Equipes.objects.filter(groupe_id=groupe_id)
    matches = Matches.objects.filter(groupe_id=groupe_id)
    new_list_matches = getMatchesByGroupe(equipes, matches)
    context = {'equipes': equipes, 'matches': new_list_matches, 'groupe_id': groupe_id}
    return HttpResponse(template.render(context, request))


def getMatchesByGroupe(equipes, matches):
    new_list = []
    name_int_equipe = ''
    name_ext_equipe = ''
    for m in matches:
        for e in equipes:
            if m.id_int_equipe == e.id:
                name_int_equipe = e.name
            if m.id_ext_equipe == e.id:
                name_ext_equipe = e.name
        data = {
            'name_int_equipe': name_int_equipe,
            'score_int_equipe': m.score_int_equipe,
            'name_ext_equipe': name_ext_equipe,
            'score_ext_equipe': m.score_ext_equipe
        }
        new_list.append(data)
    return new_list


def saveMatche(request):
    if request.method == 'POST':
        if request.POST['intEquipe'] == request.POST['extEquipe']:
            return redirect('../../Afcon/ViewMatches/' + request.POST['groupeId'])
        equipeInt = Equipes.objects.get(id=request.POST['intEquipe'])
        equipeExt = Equipes.objects.get(id=request.POST['extEquipe'])
        if request.POST['scoreIntEquipe'] == request.POST['scoreExtEquipe']:
            equipeInt.points = equipeInt.points + 1
            equipeExt.points = equipeExt.points + 1
        elif request.POST['scoreIntEquipe'] > request.POST['scoreExtEquipe']:
            equipeInt.points = equipeInt.points + 3
            equipeExt.points = equipeExt.points + 0
        else:
            equipeInt.points = equipeInt.points + 0
            equipeExt.points = equipeExt.points + 3
        equipeInt.save()
        equipeExt.save()
        matche = Matches.objects.create(
            id_int_equipe=request.POST['intEquipe'],
            score_int_equipe=request.POST['scoreIntEquipe'],
            id_ext_equipe=request.POST['extEquipe'],
            score_ext_equipe=request.POST['scoreExtEquipe'],
            groupe_id=request.POST['groupeId']
        )
        matche.save()
        return redirect('../../Afcon/groupe.html')


def ViewHuitiemeFinal(request):
    template = loader.get_template('Afcon/huitieme.html')
    allMatchesHuitiemeInt = getMatchesHuitiemeIntFinal()
    allMatchesHuitiemeExt = getMatchesHuitiemeExtFinal()
    context = {'equipeInt': allMatchesHuitiemeInt, 'equipeExt': allMatchesHuitiemeExt}
    return HttpResponse(template.render(context, request))


def getAllEquiesQualifies():
    allEquipe = Equipes.objects.all()
    allEquipeQualifiee = []
    for i in range(1, 7):
        allEquipeQualifiee.extend(allEquipe.filter(groupe_id=i).order_by("-points")[:2])
    return allEquipeQualifiee

def getMatchesHuitiemeIntFinal():
    allEquipeQualifiee = getAllEquiesQualifies()
    allMatchesHuitiemeInt = []
    allMatchesHuitiemeInt.append(allEquipeQualifiee[0])
    allMatchesHuitiemeInt.append(allEquipeQualifiee[2])
    allMatchesHuitiemeInt.append(allEquipeQualifiee[4])
    allMatchesHuitiemeInt.append(allEquipeQualifiee[6])
    allMatchesHuitiemeInt.append(allEquipeQualifiee[8])
    allMatchesHuitiemeInt.append(allEquipeQualifiee[10])
    return allMatchesHuitiemeInt

def getMatchesHuitiemeExtFinal():
    allEquipeQualifiee = getAllEquiesQualifies()
    allMatchesHuitiemeExt = []
    allMatchesHuitiemeExt.append(allEquipeQualifiee[3])
    allMatchesHuitiemeExt.append(allEquipeQualifiee[1])
    allMatchesHuitiemeExt.append(allEquipeQualifiee[7])
    allMatchesHuitiemeExt.append(allEquipeQualifiee[5])
    allMatchesHuitiemeExt.append(allEquipeQualifiee[11])
    allMatchesHuitiemeExt.append(allEquipeQualifiee[9])
    return allMatchesHuitiemeExt
