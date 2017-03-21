from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction # Your User model
		fields = '__all__'