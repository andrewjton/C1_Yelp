from django.db import models

# Create your models here.
class Transaction(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	price_range = models.IntegerField(default=0) #1 - 5
	preferences = models.CharField(max_length=1000) #csv, with tags of interest
	deals = models.IntegerField(default=0) #1 - 5
	
	listing_date = models.DateTimeField('Listing Date')
	location = models.CharField(max_length=100) #is this the best format?

	#restaurants selected?
	#name, dob, etc.?]
	def __str__(self):
		return str(self.name) + str(self.surname)