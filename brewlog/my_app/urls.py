from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('beers/', views.beers_index, name='beer-index'),
    path('beer/<int:beer_id>/', views.beer_detail, name='beer-detail'),
    path('beers/create/', views.BeerCreate.as_view(), name='beer-create'),
    path('beers/<int:pk>/update/', views.BeerUpdate.as_view(), name='beer-update'),
    path('beers/<int:pk>/delete/', views.BeerDelete.as_view(), name='beer-delete'),
    path('beer/<int:beer_id>/add-tasting/',views.add_tasting,name='add-tasting'),
    path('tastings/<int:pk>/update/', views.TastingUpdate.as_view(), name='tasting-update'),
    path('tastings/<int:pk>/delete/', views.TastingDelete.as_view(), name='tasting-delete'),
    path('accounts/signup/', views.signup, name='signup')
]
