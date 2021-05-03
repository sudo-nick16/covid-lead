from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data
from django.db.models import Q

def index(request):
    all_data = Data.objects.all()
    return render(request, 'index.html', {'all_data': all_data})

def add(request):
    return render(request, 'add.html')
#will remove add-resources functionality - cuz "reasons"

def addlead(request):
    data = Data( resources = request.POST['resources'], city = request.POST['city'], state = request.POST['state'], address = request.POST['address'],contact = request.POST['contact'])
    data.save()
    return HttpResponseRedirect('/home/')

def search(request):
    query = request.POST.get("searchbox", False)
    if query:
        all_data = Data.objects.filter(
            Q(city__icontains = query) | Q(resources__icontains = query) |Q(state__icontains = query)
            )
        return render(request, 'search.html', {'all_data': all_data, 'query': query})
    else:
        all_data = Data.objects.all()
        return HttpResponseRedirect('/home/')


