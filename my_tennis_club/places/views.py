from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
from places.models import Place
from .models import Court


def place_list(request):
    places = Place.objects.all()
    template = loader.get_template('all_places.html')
    context = {
        'places': places,
    }
    return HttpResponse(template.render(context, request))

def court_list(request):
    courts = Court.objects.all()
    return render(request, 'court_list.html', {'courts': courts})


def court_detail(request, court_id):
    court = Court.objects.get(pk=court_id)
    return render(request, 'court_detail.html', {'court': court})