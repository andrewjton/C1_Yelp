from django import forms
from .models import Transaction

class TransactionForm(forms.Form):
	name = forms.CharField(label='Your First name', max_length=20)
	surname = forms.CharField(label='Your Last name', max_length=20)
	email = forms.EmailField(label='Your e-mail', max_length=20)
	price_range = forms.IntegerField(max_value= 5, min_value=0)
	preferences = forms.CharField(label="Your Preferences", max_length=1000)
	deals = forms.IntegerField(max_value=1, min_value=0) #1 - 5

	location = forms.CharField(label="Your Preferences", max_length=200, initial="Mclean, Virginia")
	# listing_date = forms.DateTimeField()
	def __init__(self, *args, **kwargs):
	    super(TransactionForm, self).__init__(*args, **kwargs)

	    for key in self.fields:
	        self.fields['name'].required = False 
	        self.fields['surname'].required = False 
	        self.fields['email'].required = False 
	        self.fields['deals'].required = False 
