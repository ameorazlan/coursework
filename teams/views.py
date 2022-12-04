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
    context["table_list"] = tablemodel.objects.all()
    context["team_list"] = team.objects.all()
    for teamobj in team.objects.all():
        if (tablemodel.objects.filter(team=teamobj).count == 0):
            a = tablemodel.objects.create(team=teamobj)
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
