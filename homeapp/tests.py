from django.test import TestCase
from django.urls import reverse

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
        self.assertContains(response, 'This is my header')
        self.assertContains(response, 'This is My Contact Page')
        self.assertContains(response, 'This is my footer')
    def test_fixtures(self):
        response = self.client.get(reverse('fixtures'))
        self.assertEqual(response.status_code, 200)

    def test_table(self):
        response = self.client.get(reverse('table'))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        response = self.client.get(reverse('update'))
        self.assertEqual(response.status_code, 200)



