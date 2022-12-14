from django import forms
from .models import team, fixtures
# creating a form
class teamForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = team
        #Form fields corresponding to the model attributes
        fields = ['name', 'player_count', 'year_founded', 'owner_email', 'image']
        widgets = {
        'name': forms.TextInput(attrs={
        'class': 'formfield',
        'placeholder': 'Team Name',
        }),
        'player_count': forms.NumberInput(attrs={
        'class': 'formfield',
        'placeholder': 'Player Count',
        }),
        'year_founded': forms.NumberInput(attrs={
        'class': 'formfield',
        'placeholder': 'Year Founded',
        }),
        'owner_email': forms.TextInput(attrs={
        'class': 'formfield',
        'placeholder': 'Owner Email',
        }),
    }

class fixtureForm(forms.ModelForm):
     class Meta:
        # specify model to be used
        model = fixtures
        #Form fields corresponding to the model attributes
        fields = ['team1', 'team2', 'score1', 'score2']
        widgets = {
        'team1': forms.NumberInput(attrs={
        'class': 'formfield',
        'placeholder': 'Team1 ID',
        }),
        'team2': forms.NumberInput(attrs={
        'class': 'formfield',
        'placeholder': 'Team2 ID',
        }),
        'score1': forms.NumberInput(attrs={
        'class': 'formfield',
        'placeholder': 'Team1 Score',
        }),
        'score2': forms.NumberInput(attrs={
        'class': 'formfield',
        'placeholder': 'Team2 Score',
        }),
    }