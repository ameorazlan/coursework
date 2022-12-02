from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib import messages
from .models import team
from .forms import teamForm


# Create your views here.
def fixtures(request):
    context = {}
    return render(request, 'teams/fixtures.html', context)

def table(request):
    context = {}
    return render(request, 'teams/table.html', context)

def teams(request):
    context = {}
    context["team_list"] = team.objects.all()
    return render(request, "teams/teams.html",context)


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
