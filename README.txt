AVIDALAB CLOUD

AvidaLab Cloud is a web interface tool built to aid in the analysis of data that comes out of the Avida eveolutionary biology software. Users
may configure nearly all aspects of Avida to accommodate the needs of an experiment. System configurations include the size of the world,
the length of the experiment, the presence and behavior of resources, mutation rates, organism age limit, and many otherfactors. In 
addition, users can record many different statistics during the experimental run,recorded in plain text files. This information is then 
analyzed after the experiment has ended.

PREREQUISITES 

AvidaLab cloud assumes that you have Python 3 or greater as well as the Django web framework version 1.11 or installed on your computer.
For help with installing please see the following sites: https://www.python.org/ for python and https://www.djangoproject.com/ for Django.

PACKAGES

- coverage 4.3.4
- django-nose 1.4.4
- matplotlib 2.0.2
- natsort 5.0.3
- numpy 1.12.1
- patool 1.12
- pyunpack 0.1.2
- scipy 0.19.0
- selenium 3.3.3

RUNNING AVIDALAB CLOUD 

1. Clone the project from https://github.com/JeremyFlorence/AvidaLab.git
2. Install all required packages via pip.
3. Open a terminal in the directory containing manage.py, and run the following command "python manage.py runserver"
4. Open a browser and go to to "localhost:8000".


