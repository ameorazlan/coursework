from django.test import TestCase
from django.urls import reverse
from django.core.mail import send_mail
from django.core import mail

# Create your tests here.
class HomePageTests(TestCase):
    def setUp(self):
        return
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    
    def test_fixtures(self):
        response = self.client.get(reverse('fixtures'))
        self.assertEqual(response.status_code, 200)

    def test_table(self):
        response = self.client.get(reverse('table'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
    
    def test_teams(self):
        response = self.client.get(reverse('teams'))
        self.assertEqual(response.status_code, 200)
    
    def register_fixture(self):
        response = self.client.get(reverse('register_fixture'))
        self.assertEqual(response.status_code, 200)

class MailerTests(TestCase):
    def test_send_email(self):
        send_mail('Testing', 'Testing', 'from@testing.com', ['am03864@surrey.ac.uk'])
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Testing')

