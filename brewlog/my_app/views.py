from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import Beer, Tasting
from .forms import TastingForm
from django.urls import reverse_lazy


def home (request):
    return render(request,'home.html')

def beers_index(request):
    beers=Beer.objects.all()
    return render(request,'beers/index.html',{'beers':beers})

def beer_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    tastings = beer.tasting_set.all()
    tasting_form = TastingForm()
    return render(request, 'beers/detail.html', {
        'beer': beer,
        'tastings': tastings,
        'tasting_form': tasting_form
    })


def add_tasting(request, beer_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit=False)
        new_tasting.beer_id = beer_id
        new_tasting.save()
    return redirect('beer-detail', beer_id=beer_id)


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

class TastingUpdate(UpdateView):
    model = Tasting
    fields = ['name', 'address', 'city', 'state', 'zip']
    template_name = 'tasting_form.html'

class TastingDelete(DeleteView):
    model=Tasting
    template_name = 'tasting_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('beer-detail', kwargs={'beer_id': self.object.beer.id})

