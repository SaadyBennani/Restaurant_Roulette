from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Business_Search, Queue
import requests
import json


# Create your views here.


def index(request):
    return render(request, 'resto_roulette/index.html')

def queue(request):
    # if Queue.objects.filter(user=request.user).exists():
    #     queue = Queue.objects.get(user=request.user)
    # # else:
    # #     queue = Queue(user=request.user, biz_data='')
    # #     queue.save()
    #
    # # response = JsonResponse(biz_queue, safe=False)
    # context = {
    #     'biz_queue': queue.biz_data
    # }
    # print(context)
    # return render(request, 'resto_roulette/queue.html', context)
    return render(request, 'resto_roulette/queue.html')


def add_to_queue(request):
    if request.method == 'POST':
        biz_queue = json.loads(request.body).get('biz_queue')
        print(biz_queue)
        if Queue.objects.filter(user=request.user).exists():
            print('exists')
            queue = Queue.objects.get(user=request.user)
            queue.add(biz_queue)
        else:
            print('creating')
            queue = Queue(user=request.user, biz_data=json.dumps(biz_queue))
            queue.save()
    else:
        queue = Queue.objects.get(user=request.user)
    return JsonResponse(queue.biz_data, safe=False)

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
