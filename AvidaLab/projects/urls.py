from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^$', views.projects_page, name='projects'),
    url(r'^experiments/$', views.experiments_page, name='experiments'),
    url(r'^runs/$', views.runs_page, name='runs'),
    url(r'^data/$', views.data_page, name='data'),
]