from django.urls import path
from . import views

urlpatterns = [
    path('', views.buildSite, name='index'),
    path('about-us', views.buildAboutUs, name='about-us'),
    path('contact-us', views.buildContactUs, name='contact-us'),
    path('projects', views.buildProjects, name='projects'),
    path('project/<int:id>', views.buildProjectDetails, name='project'),
    path('publications', views.buildPublications, name='publications'),
    path('send-message', views.buildContactUs, name='contact'),
    path('publication/<int:id>', views.buildPublicationDetails, name='publication'),
    path('success', views.buildSuccessPage, name='success')
]