from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import Beer

def home (request):
    return render(request,'home.html')

def beers_index(request):
    beers=Beer.objects.all()
    return render(request,'beers/index.html',{'beers':beers})

def beer_detail(request,beer_id):
    beer=Beer.objects.get(id=beer_id)
    return render(request,'beers/detail.html',{'beer':beer})

class BeerCreate(CreateView):
    model=Beer
    fields='__all__'
    template_name = 'main_app/beer_form.html'


class BeerUpdate(UpdateView):
    model=Beer
    fields='__all__'
    template_name = 'main_app/beer_form.html'

class BeerDelete(DeleteView):
    model=Beer
    template_name = 'main_app/beer_confirm_delete.html'
    success_url="/beers/"

