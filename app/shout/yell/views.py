from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from .forms import TransactionForm
from .models import Transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from .scripts.yelp_fusion_api import *

import time

# Create your views here.


def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransactionForm(request.POST, initial={'location': 'Charlottesville, Virginia'})
        # check whether it's valid:
        if form.is_valid():
            # print(form.cleaned_data['name'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            name = request.POST.get('name', '')
            surname = request.POST.get('surname', '')
            email = request.POST.get('email', '')
            preferences = request.POST.get('preferences', '')
            price_range = request.POST.get('price_range', '')
            if (request.POST.get('deals', '')):
                deals = request.POST.get('deals', '')
            else:
            	deals = 0
            listing_date = timezone.now()
            location = request.POST.get('location', '')
            
            transaction= Transaction(name=name, surname=surname, preferences=preferences, price_range=price_range, deals=deals, listing_date=listing_date, location = location)
            transaction.save()
            # data = serializers.serialize("json", Transaction.objects.filter(pk=transaction.id))
            data = (transaction).__dict__
            print(data)
            return render_to_response('testing_ajax/ajax_template.html', {'json': data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    return render(request, 'testing_ajax/signup_awesome.html', {'form': form})

def testing(request):
	return HttpResponse('Hi! This feature is still in testing. The goal is to visualize the dining preferences of users around the world using their sanitized data.')

def restaurants(request):
    return render(request, 'testing_ajax/ajax_template.html')    

@csrf_exempt
def yelp_api(request):
    time.sleep(1)
    if request.method != 'POST':
        return _error_response(request, "must make POST request")
    # if 'username' not in request.POST or \
    #     'Socialcorp' not in request.POST or \
    #     'quantity' not in request.POST:
    #     return _error_response(request, "missing required paramaters")
    
    #check if company  & username exists\
    print(request)
    print(request.POST)
    print("preferences: " + request.POST.get('preferences', ''))
    print("longitude: " + request.POST.get('longitude', str(150.644)))
    print("latitude: " + request.POST.get('latitude', str(-34.397)))
    try:
        restaurants = query_api(request.POST.get('preferences', 'taco'), request.POST.get('longitude', str(150.644)), request.POST.get('latitude', str(-34.397)))
        restaurants = json.dumps(restaurants)
        restaurants = json.loads(restaurants)
        pass
    except:
        return _error_response(request, "company or username does not exist")
    
    return _success_response(request, restaurants)

#yelp fusion api
@csrf_exempt
def query_api(preferences, longitude, latitude):
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    return search(bearer_token, preferences, longitude, latitude) #add more preferences

@csrf_exempt
def _error_response(request, error_msg):
    return JsonResponse({'ok': False, 'resp': error_msg})

@csrf_exempt
def _success_response(request, resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})