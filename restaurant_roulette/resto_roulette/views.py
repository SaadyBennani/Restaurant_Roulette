from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Business_Search
from .forms import BusinessForm
from .YelpAPI import API_KEY
import requests


# Create your views here.


def index(request):
    return render(request, 'resto_roulette/index.html')

def cards(request):
    return render(request, 'resto_roulette/cards.html')

def search_results(request):
    pass

def Business_search(request):
    form = BusinessForm(request.POST or None)
    if request.method == 'POST':
        search_results = []
        if form.is_valid():
            cat = request.POST['biz_category']
            loc = request.POST['location']
            search = Business_Search(biz_category=cat, location=loc)
            form = BusinessForm()

            business = []

            search_results = API_search(cat, loc)
            print(search_results)
            review_results_total = []

            for idx, business in enumerate(search_results):
                biz_id = business['id']
                review_results = Review_search(biz_id)
                search_results[idx]['reviews'] = review_results
                review_results_total.append(review_results)
            print(review_results)

        context = {
            'form': form,
            'search_results': search_results,
            'businesses': [],
            'review_results_total': review_results_total,
        }
        return render(request, 'resto_roulette/search_results.html', context)

    return render(request, 'resto_roulette/biz_search.html', {'form': form})


def API_search(cat, loc):
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' % API_KEY}
    parameters = {'term': cat, 'location': loc,
                  'limit': 5,
                  'radius': 10000}
    response = requests.get(url=endpoint, params=parameters, headers=headers)
    business_data = response.json()
    return business_data['businesses']


def Review_search(biz_id):
    endpoint = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(biz_id)
    headers = {'Authorization': 'bearer %s' % API_KEY}
    response = requests.get(url=endpoint, headers=headers)
    review_data = response.json()
    return review_data['reviews']
