from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.analysis_page, name='analysis')
]