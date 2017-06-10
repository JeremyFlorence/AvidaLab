from django.db import models
import os

# Project Model
class Project(models.Model):

    # Name of the project
    name = models.CharField(max_length=255)

    # File associated with project
    dataFile = models.FileField(upload_to='projects/')

    # Path to the extracted data
    extractPath = models.TextField(default='null')

    # Name of the file
    def fileName(self):
        return os.path.basename(self.dataFile.name)

    def delete(self, *args, **kwargs):
        self.dataFile.delete()
        super(Project, self).delete(*args, **kwargs)