from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beers/', views.beers_index, name='beer-index'),
    path('beer/<int:beer_id>/', views.beer_detail, name='beer-detail'),
    path('beers/create/', views.BeerCreate.as_view(), name='beer-create'),
    path('beers/<int:pk>/update/', views.BeerUpdate.as_view(), name='beer-update'),
    path('beers/<int:pk>/delete/', views.BeerDelete.as_view(), name='beer-delete'),
]
