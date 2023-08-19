from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse


# Create your views here.

def buildSite(request):
    services = Service.objects.all()
    sliders = Slider.objects.all().order_by('position')
    testimonials = Testimonial.objects.all()
    context = {
        'current_screen': 'index',
        'services': services,
        'sliders': {
            'count': range(1, sliders.count() + 1),
            'objects': sliders
        },
        'testimonials': {
            'count': range(testimonials.count()),
            'objects': testimonials
        }
    }
    return render(request, 'index.html', context)


def buildAboutUs(request):
    members = TeamMember.objects.all()
    context = {
        'current_screen': 'about-us',
        'members': members
    }
    return render(request, 'about_us.html', context)


def buildContactUs(request):
    context = {
        'current_screen': 'contact-us'
    }
    return render(request, 'contact_us.html', context)


def buildProjects(request) -> object:
    projects = Project.objects.all()
    context = {
        'current_screen': 'projects',
        'projects': projects

    }
    return render(request, 'projects.html', context)


def buildProjectDetails(request, id):
    project = Project.objects.get(id=id)
    images = ProjectImage.objects.filter(project=project).all()
    context = {
        'current_screen': 'project_details',
        'project': project,
        'images': images
    }
    return render(request, 'project_detail.html', context)


def buildPublications(request):
    publicationObjects = Publication.objects.all()
    publications = publicationObjects.filter(publication_type=enums.PublicationType.PUBLICATION.name).all()
    journals = publicationObjects.filter(publication_type=enums.PublicationType.JOURNAL.name).all()
    books = publicationObjects.filter(publication_type=enums.PublicationType.BOOK.name).all()
    conferences = Conference.objects.all()
    context = {
        'current_screen': 'publications',
        'publications': publications,
        'books': books,
        'journals': journals,
        'conferences': conferences
    }
    return render(request, 'publications.html', context)


def buildPublicationDetails(request, id):
    publication = Publication.objects.get(id=id)
    context = {
        'current_screen': 'publication_details',
        'publication': publication,
    }
    return render(request, 'publication_detail.html', context)
