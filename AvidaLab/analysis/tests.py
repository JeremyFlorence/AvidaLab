import time
from django.core.urlresolvers import resolve
from django.test import TestCase
from selenium import webdriver

from Analysis.views import analysis_view


# Create your tests here.


class AnalysisPageTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # tests to make sure analysis page loads correct view
    def test_url_resolves_to_analysis_view(self):
        found = resolve('/analysis/')
        self.assertEqual(found.func, analysis_view)
        self.browser.close()

    # tests that page shows correct HTML
    def test_Analysis_view_returns_correct_html(self):
        response = self.client.get('/analysis/')
        self.assertTemplateUsed(response, 'Analysis/selects.html')
        self.browser.close()

    # tests "home" link links to home
    # def test_link_to_homepage(self):
    #     link = self.browser.find_element_by_id("Home")
    #     link.click()
    #
    #     time.sleep(2)
    #     self.assertIn('AvidaLab', self.browser.title)
    #     self.browser.close()
