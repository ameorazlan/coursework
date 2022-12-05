from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    context = {}
    return render(request, 'homeapp/home.html', context)

#Deals with contact view and contact form submissions
def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        #If form is valid, then try to send mail to the admin email
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = name + ':\n' + form.cleaned_data['message']
            try:
                send_mail(subject,message,email, ['am03864@surrey.ac.uk'])
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'Message Not Sent')
                return HttpResponse("Invalid header found.")
            #Display success message if mail got sent
            messages.add_message(request, messages.SUCCESS, 'Message Successfuly Sent')
            return redirect(reverse('home'))
        else:
            #Display error message if form is invalid
            messages.add_message(request, messages.ERROR, 'Invalid Form Data. Message Not Sent') 
    return render(request, 'homeapp/contact.html', {"form":form})
