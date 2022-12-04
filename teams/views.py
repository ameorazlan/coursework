from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib import messages
from .models import team, table as tablemodel
from .forms import teamForm, fixtureForm


# Create your views here.
def fixtures(request):
    context = {}
    return render(request, 'teams/fixtures.html', context)

def table(request):
    context = {}
    context["table_list"] = tablemodel.objects.all().order_by('-score')
    context["team_list"] = team.objects.all()
    for teamobj in team.objects.all():
        if (not tablemodel.objects.filter(team_id=teamobj.id).exists()):
            a = tablemodel.objects.create(team_id=teamobj.id)
            a.save()
    return render(request, 'teams/table.html', context)

def teams(request):
    context = {}
    context["team_list"] = team.objects.all()
    return render(request, "teams/teams.html",context)

def register_fixture(request):
    context = {}
    form = fixtureForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            team1ID = form.cleaned_data['team1']
            team2ID = form.cleaned_data['team2']
            score1 = form.cleaned_data['score1']
            score2 = form.cleaned_data['score2']
            team1 = tablemodel.objects.get(team_id=team1ID)
            team2 = tablemodel.objects.get(team_id=team2ID)
            team1.GP += 1
            team2.GP += 1
            team1.GF += score1
            team1.GA += score2
            team2.GF += score2
            team2.GA += score1
            if score1 > score2:
                team1.wins += 1
                team2.loses += 1
                team1.score += 3
            elif score2 > score1:
                team1.loses += 1
                team2.wins += 1
                team2.score += 3
            else:
                team1.draws +=1
                team2.draws += 1
                team1.score += 1
                team2. score += 1
            team1.save()
            team2.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Fixture Registered')
            return redirect('fixtures')
    context['form']= form
    context["team_list"] = team.objects.all()
    return render(request, "teams/register_fixture.html",context)


def create(request):
    context ={}
    form = teamForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Team Registered')
            return redirect('teams')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Team not registered')
    context['form']= form
    return render(request, "teams/create.html", context)
