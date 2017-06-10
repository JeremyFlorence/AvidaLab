from django import forms
from . models import Project

class NewProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = '__all__'
    
    name = forms.CharField(required=True)
    
    dataFile = forms.FileField(label='Select a file')