from django.test import TestCase
from django.core.urlresolvers import resolve
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from contact.views import contact_view
# Tests.

class ContactPageTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_url_resolves_to_contact_view(self):
        page = resolve('/contact/')
        self.assertEqual(page.func, contact_view)
        self.browser.close()
		
    def test_contact_view_returns_correct_html(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact/Contacts.html')
        self.browser.close()
		
    def test_link_to_home_page(self):
        self.browser.get('http://127.0.0.1:8080/contact/')
        link = self.browser.find_element_by_id("Home-link")
        link.click()
        time.sleep(2)
        self.assertIn('AvidaLab', self.browser.title)
        self.browser.close()


    def test_link_to_contact_page(self):
        self.browser.get('http://127.0.0.1:8080/contact/')
        link = self.browser.find_element_by_id("Contact-link")
        link.click()
        time.sleep(2)
        self.assertIn('Contact', self.browser.title)
        self.browser.close()

    def test_link_to_projects_page(self):
        self.browser.get('http://127.0.0.1:8080/contact/')
        link = self.browser.find_element_by_id("Projects-link")
        link.click()
        time.sleep(2)
        self.assertIn('Projects', self.browser.title)
        self.browser.close()

    def tearDown(self):
        self.browser.quit()