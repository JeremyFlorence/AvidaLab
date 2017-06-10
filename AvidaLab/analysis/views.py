from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from projects.models import Project
from projects import tools
from projects import getStats as stats

# The page where the user can see the results of the analysis
def analysis_page(request):
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
        runs = request.POST.getlist('run')

        # Get all of the data from each run and average it together to smooth it out
        var1_data = tools.get_mean_column(project, experiment, runs, data_file, var1)
        var2_data = tools.get_mean_column(project, experiment, runs, data_file, var2)

        tools.line_graph(var1, var1_data, var2, var2_data, project.name)
        mean = stats.findStats(var2_data, 'mean')
        median = stats.findStats(var2_data, 'median')
        stdev = stats.findStats(var2_data, 'stdev')

        return render(
            request,
            'analysis.html',
            {'projectPK': projectPK, 
            'experiment': experiment, 
            'data_file': data_file,
            'runs': runs,
            'var1': var1,
            'var2': var2,
            'mean': mean,
            'median': median,
            'stdev': stdev
            }
        )
    else:
        return HttpResponseRedirect(reverse('projects'))