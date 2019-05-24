from django.urls import path
from . import views

app_name = 'resto_roulette'  # for namespacing
urlpatterns = [
    path('', views.index, name='home_view'),
    path('search', views.Business_search, name='biz_search'),
    path('queue', views.queue, name='queue'),

]
