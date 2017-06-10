from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from home.views import home_view

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_view)

    def test_home_view_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/welcome.html')
