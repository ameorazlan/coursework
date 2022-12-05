from django.test import TestCase
from django.urls import reverse
from django.core.mail import send_mail
from django.core import mail

# Testing all the template pages
#Checks if the reponse code is successful, and a few content checks including navbar and footer
class TemplateTests(TestCase):
    def setUp(self):
        return
    #Tests home page
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the University Football League South Division')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')

    #Tests contacts page
    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact us with any queries')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')
    
    #Tests fixtures page
    def test_fixtures(self):
        response = self.client.get(reverse('fixtures'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Team Name')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')

    def test_table(self):
        response = self.client.get(reverse('table'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Team ID')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')

    #Tests team creation page
    def test_create(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register your team here')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')
    
    #Tests teams view page
    def test_teams(self):
        response = self.client.get(reverse('teams'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Team Logo')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')
    
    #Tests fixture registration page
    def register_fixture(self):
        response = self.client.get(reverse('register_fixture'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register your fixture here')
        self.assertContains(response, 'Home')
        self.assertContains(response, '2022 Adam Meor Azlan')

    #Tests the mailer system
class MailerTests(TestCase):
    def test_send_email(self):
        send_mail('Testing', 'Testing', 'from@testing.com', ['am03864@surrey.ac.uk'])
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Testing')

