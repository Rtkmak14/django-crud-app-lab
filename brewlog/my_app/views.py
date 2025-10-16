from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import Beer, Tasting
from .forms import TastingForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'

@login_required
def beers_index(request):
    beers=Beer.objects.filter(user=request.user)
    return render(request,'beers/index.html',{'beers':beers})

@login_required
def beer_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    tastings = beer.tasting_set.all()
    tasting_form = TastingForm()
    return render(request, 'beers/detail.html', {
        'beer': beer,
        'tastings': tastings,
        'tasting_form': tasting_form
    })

@login_required
def add_tasting(request, beer_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit=False)
        new_tasting.beer_id = beer_id
        new_tasting.save()
    return redirect('beer-detail', beer_id=beer_id)


class BeerCreate(LoginRequiredMixin,CreateView):
    model=Beer
    fields=['name', 'brewery', 'style', 'notes']
    template_name = 'main_app/beer_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BeerUpdate(LoginRequiredMixin,UpdateView):
    model=Beer
    fields=['name', 'brewery', 'style', 'notes']
    template_name = 'main_app/beer_form.html'

class BeerDelete(LoginRequiredMixin,DeleteView):
    model=Beer
    template_name = 'main_app/beer_confirm_delete.html'
    success_url="/beers/"

class TastingUpdate(LoginRequiredMixin,UpdateView):
    model = Tasting
    fields = ['name', 'address', 'city', 'state', 'zip']
    template_name = 'tasting_form.html'

class TastingDelete(LoginRequiredMixin,DeleteView):
    model=Tasting
    template_name = 'tasting_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('beer-detail', kwargs={'beer_id': self.object.beer.id})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('beer-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    