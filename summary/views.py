from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import Http404
from django.shortcuts import render
import json

with open(staticfiles_storage.path('data/language_version.json'), 'r') as json_file:
    data = json.load(json_file)

# Create your views here.
def index(request, lang="en"):
    try:
        context = data[lang]
    except KeyError as err:
        raise Http404("Language not implemented yet")
    return render(request, 'summary/index.html', context)
