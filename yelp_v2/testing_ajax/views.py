from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import TransactionForm
from .models import Transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
# Create your views here.



class SignUpView(CreateView):
    template_name = 'testing_ajax/signup.html'
    form_class = UserCreationForm




def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def transaction(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransactionForm(request.POST, initial={'location': 'Charlottesville, Virginia'})
        # check whether it's valid:
        print("Request: ------------")
        print(request.POST)
        print("Form Errors: ------------")
        print(form.errors)
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
            
            return HttpResponseRedirect('/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    return render(request, 'testing_ajax/signup_awesome.html', {'form': form})

def success(request):
	return HttpResponse('Congrats dude')
