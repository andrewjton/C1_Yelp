from django.db import models

# Create your models here.
class Transaction(models.Model):
	description = models.CharField(max_length=1000) #csv, with tags of interest
	price_range = models.IntegerField(default=0) #1 - 5
	listing_date = models.DateTimeField('Listing Date')
	location = models.CharField(max_length=100) #is this the best format?
	#restaurants selected?
	#name, dob, etc.?]
	def __str__(self):
		return str(self.id)