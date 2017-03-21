from django.shortcuts import render
from .models import Transaction
from .forms import TransactionForm, TransactionForm2
from django.utils import timezone

# Create your views here.

def first(request):
	if request.method == "POST":
		form = TransactionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.price_range = request.price_range
			post.description = request.description
			post.location = request.location
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = TransactionForm()
	return render(request, 'crispyforms_test/first.html', {'form': form})

def second(request):
	if request.method == "POST":
		form = TransactionForm2(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.price_range = request.price_range
			post.description = request.description
			post.location = request.location
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = TransactionForm2()
	return render(request, 'crispyforms_test/second.html', {'form': form})
