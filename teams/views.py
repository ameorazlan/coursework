from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib import messages
from .models import team, table as tablemodel, fixtures as fixturesmodel
from .forms import teamForm, fixtureForm


#Returns all fixtures by descending ID, so most recent ones on top
def fixtures(request):
    context = {}
    context['fixtures_list'] = fixturesmodel.objects.all().order_by('-id')
    context["team_list"] = team.objects.all()
    return render(request, 'teams/fixtures.html', context)

#Returns the table with descending team points
def table(request):
    context = {}
    context["table_list"] = tablemodel.objects.all().order_by('-score')
    context["team_list"] = team.objects.all()
    #Updates the table model to make sure it includes all the teams
    for teamobj in team.objects.all():
        if (not tablemodel.objects.filter(team_id=teamobj.id).exists()):
            a = tablemodel.objects.create(team_id=teamobj.id)
            a.save()
    return render(request, 'teams/table.html', context)

#Retruns a list of all teams
def teams(request):
    context = {}
    context["team_list"] = team.objects.all()
    return render(request, "teams/teams.html",context)

#Dealing with fixture registration form
def register_fixture(request):
    context = {}
    form = fixtureForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            #Save the form data to variables which are used to update the table database
            team1ID = form.cleaned_data['team1']
            team2ID = form.cleaned_data['team2']
            score1 = form.cleaned_data['score1']
            score2 = form.cleaned_data['score2']
            team1 = tablemodel.objects.get(team_id=team1ID)
            team2 = tablemodel.objects.get(team_id=team2ID)
            #Add 1 to both team's games played
            team1.GP += 1
            team2.GP += 1
            #Add the corresponding goals to their total goals scored
            team1.GF += score1
            team1.GA += score2
            team2.GF += score2
            team2.GA += score1
            #Gives the teams points depending on if they win, lose, or tie
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
            #Save the data to database
            team1.save()
            team2.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Fixture Registered')
            return redirect('fixtures')
    context['form']= form
    context["team_list"] = team.objects.all()
    return render(request, "teams/register_fixture.html",context)

#Deals with team creation form
def create(request):
    context ={}
    form = teamForm(request.POST or None)
    if(request.method == 'POST'):
        form = teamForm(request.POST, request.FILES)
        #If form is valid, then save the data to teams database and display success message
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Team Registered')
            return redirect('table')
        #Otherwise display error message
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Team not registered')
    context['form']= form
    return render(request, "teams/create.html", context)
