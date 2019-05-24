from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Business_Search
import requests
import json


# Create your views here.


def index(request):
    return render(request, 'resto_roulette/index.html')

def queue(request):
    if request.method == 'POST':
        biz_queue = json.loads(request.body)
        # response = JsonResponse(biz_queue, safe=False)
        context = {
            'biz_queue': JsonResponse(biz_queue, safe=False)
        }
        print(context)
        print(biz_queue)
        return render(request, 'resto_roulette/queue.html', context)
    return render(request, 'resto_roulette/queue.html')





def Business_search(request):
    if request.method == 'POST':
        print(request.POST)
        context = {
            'what': request.POST.get('what'),
            'where': request.POST.get('where')
        }

        print(context['what'])
        print(context['where'])


        return render(request, 'resto_roulette/search_results.html', context)

    return render(request, 'resto_roulette/biz_search.html')


def Review_search(biz_id):
    endpoint = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(biz_id)
    headers = {'Authorization': 'bearer %s' % API_KEY}
    response = requests.get(url=endpoint, headers=headers)
    review_data = response.json()
    return review_data['reviews']
