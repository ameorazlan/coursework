from django import forms
#Form for contacting the website admins
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Name',}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield', 'placeholder': 'Subject',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'formfield','placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'formfield', 'placeholder': 'Message',}), required=True)

