import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_welcome_page_and_start_project(self):
        wait_time = 2
        
        # User opens AvidaLab homepage
        self.browser.get('http:/localhost:8000')

        # User sees the page title and header mention AvidaLab by TeamJACKS
        self.assertIn('AvidaLab', self.browser.title)

        h1 = self.browser.find_element_by_tag_name('h1')
        devs = self.browser.find_element_by_id('devs')
        p = self.browser.find_element_by_tag_name('p')

        self.assertIn('Welcome To AvidaLab', h1.text)
        self.assertIn('By: TeamJACKS', devs.text)
        self.assertIn("Avida Labs currently just opens. We'll update as this gets better!", p.text)
        self.browser.close(self)

        time.sleep(wait_time)

        # User is now on the Projects page
        self.assertIn('Projects', self.browser.title)
        self.browser.close(self)

if __name__ == '__main__':

    #port = input("Please enter Port Number: ")
    unittest.main(warnings='ignore')
    unittest.main(warnings='ignore')