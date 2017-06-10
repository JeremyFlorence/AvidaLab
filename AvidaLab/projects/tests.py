from django.core.urlresolvers import resolve
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from projects.views import projects_page
from projects import tools
from . models import Project
from . forms import NewProjectForm
import os.path
import shutil

# Create your tests here.
class ProjectsPageTest(TestCase):

    def test_projects_url_resolves_to_projects_page_view(self):
        found = resolve('/projects/')
        self.assertEqual(found.func, projects_page)

    def test_projects_page_returns_correct_html(self):
        response = self.client.get('/projects/')
        self.assertTemplateUsed(response, 'projects.html')

    def test_Project_model(self):
        test_project = Project(name='Test', dataFile='AvidaLab/projects/projects/test.txt', extractPath = os.path.join('projects', 'data', 'Test'))

        self.assertTrue(test_project.name == 'Test')
        self.assertTrue(test_project.dataFile == 'AvidaLab/projects/projects/test.txt')
        self.assertTrue(test_project.extractPath == 'projects/data/Test')
    
    # Takes a test zip archive and checks to see that it gets extracted to the right place using
    # our unzipping function
    def test_unzipping(self):
        test_project = Project(name='Test', dataFile='AvidaLab/projects/uploads/test.zip', extractPath = os.path.join('projects', 'data', 'Test'))
        tools.main('projects/uploads/testdata/test.zip', test_project.name)
        self.assertTrue(os.path.exists(test_project.extractPath))
        dataPath = os.listdir(test_project.extractPath)
        print(dataPath)
        shutil.rmtree('projects/data/' + test_project.name)




