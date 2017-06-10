from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from . models import Project
from . forms import NewProjectForm
from projects import tools
from pathlib import os
from natsort import natsorted
import time


# The page where you create or select a project
def projects_page(request):
    # If the user fills out the form with valid data, we'll add their
    # project to the database
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newProject = Project(dataFile=request.FILES['dataFile'], 
                                name=form['name'].value(), 
                                extractPath=os.path.join('projects', 'data', form['name'].value()))
            newProject.save()

            # extract all of the contents up the uploaded data archive
            tools.decompress('projects/uploads/projects/' + newProject.fileName(), newProject.name)

            # Redirect to the projects page after POST
            return HttpResponseRedirect(reverse('projects'))
    else:
        form = NewProjectForm()  # An empty, unbound form

    # List of existing projects
    projects = Project.objects.all()

    return render(
        request,
        'projects.html',
        {'projects': projects, 'form': form}
    )

# The page where you select and experiment and data file to use
def experiments_page(request):
    # Users can only get to this page by filling out the required form.
    # If a user tries to access this url through their browser without
    # filling out the form, we'll redirect them back to the projects page.
    if request.method == 'POST':
        projectPK = request.POST.get('project')
        project = Project.objects.get(pk=projectPK)

        # We need to get a list of experiments in the project directory
        # to give to the user as options
        experiments_dir = os.path.join(project.extractPath, 'sg_reruns/')
        experiments = tools.check_folders(experiments_dir)

        return render(
            request,
            'experiments.html',
            {'projectPK': projectPK, 'experiments': experiments}
        )
    else:
        return HttpResponseRedirect(reverse('projects'))

# The page where the user selects their data variables they want to analyze
def data_page(request):
    # Users can only get to this page by filling out the required form.
    # If a user tries to access this url through their browser without
    # filling out the form, we'll redirect them back to the projects page.
    if request.method == 'POST':
        projectPK = request.POST.get('project')
        project = Project.objects.get(pk=projectPK)
        experiment = request.POST.get("experiment")
        data_file = request.POST.get('data_file')
        runs = request.POST.getlist('run')

        # We need a list of column headers from the selected file
        # to give to the user as options.
        column_headers = tools.get_headers(project, data_file)

        return render(
            request,
            'data.html',
            {'projectPK': projectPK, 
            'experiment': experiment, 
            'data_file': data_file,
            'headers': column_headers}
        )
    else:
        return HttpResponseRedirect(reverse('projects'))

# The page where the user selects the runs they want to use
def runs_page(request):
    # Users can only get to this page by filling out the required form.
    # If a user tries to access this url through their browser without
    # filling out the form, we'll redirect them back to the projects page.
    if request.method == 'POST':
        projectPK = request.POST.get('project')
        project = Project.objects.get(pk=projectPK)
        experiment = request.POST.get("experiment")
        data_file = request.POST.get('data_file')
        var1 = request.POST.get('var1')
        var2 = request.POST.get('var2')
        experiments_dir = os.path.join(project.extractPath, 'sg_reruns/')
        runs = tools.check_folders(os.path.join(experiments_dir, experiment))
        runs = natsorted(runs)

        return render(
            request,
            'runs.html',
            {'projectPK': projectPK, 
            'experiment': experiment, 
            'data_file': data_file,
            'runs': runs,
            'var1': var1,
            'var2': var2}
        )
    else:
        return HttpResponseRedirect(reverse('projects'))