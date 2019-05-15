from django.urls import path
from . import views

app_name = 'resto_roulette'  # for namespacing
urlpatterns = [
    path('home', views.index, name='home_view'),
    path('', views.Business_search, name='biz_search'),
    path('search-results', views.search_results, name='search_results'),
    path('cards', views.cards, name='cards'),
]
