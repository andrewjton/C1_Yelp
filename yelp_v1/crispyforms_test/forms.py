from django import forms
from .models import Transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction # Your User model
		fields = '__all__'
		

class TransactionForm2(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = False
	helper.layout = Layout(
		TabHolder(
			Tab(
				'ONE',
				'description',
			),
			Tab(
				'TWO',
				'price_range',
			),
			Tab(
				'THREE',
				'location',
				'listing_date',
			)
		)
	)

	class Meta:
		model = Transaction # Your User model
		fields = '__all__'
