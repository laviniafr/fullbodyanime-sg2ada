from django.shortcuts import render
from gallery.models import Sample, Prototype
from django.template import loader
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {
        'random_num': random.randint(1,922)
    }
    return render(request, 'generate_index.html', context)

def about(request):
    return render(request, 'about.html')

def prototype_detail(request, p):
    prototype = Prototype.objects.get(pk=p)
    context = {
        'prototype' : prototype,
        'random_num': random.randint(1,922),
    }
    return render(request, 'prototype_detail.html', context)

def gallery_index(request):
    samples = Sample.objects.all()
    context = {
        'samples': samples
    }
    return render(request, 'gallery_index.html', context)

def sample_detail(request, pk):
    sample = Sample.objects.get(pk=pk)
    context = {
        'sample' : sample,
        'random_num': random.randint(1,922),
    }
    return render(request, 'sample_detail.html', context)

def add_sample(request):
    if request.method == 'POST':
        id = request.POST.get("new_sample"," ")
        new_sample = Prototype.objects.get(pk=id)
        sample = Sample.objects.create(title = new_sample.title, image = new_sample.image, description="Sample selected by anonymous user.")
        return HttpResponseRedirect(reverse('gallery_index'))

