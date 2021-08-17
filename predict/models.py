from django.db import models


class PredResults(models.Model):
	CATEGORY=[('es_barsandrestaurants','es_barsandrestaurants'),
		('es_contents','es_contents'),
		('es_fashion','es_fashion'),
		('es_food','es_food' ),
		('es_health','es_health'),
		('es_home','es_home'),
		('es_hotelservices','es_hotelservices'),
		('es_hyper', 'es_hyper'),
		('es_leisure','es_leisure'),
		('es_otherservices','es_otherservices'),
		('es_sportsandtoys','es_sportsandtoys'),
		('es_tech','es_tech'),
		('es_transportation','es_transportation'),
		('es_travel','es_travel'),
		('es_wellnessandbeauty','es_wellnessandbeauty'),]
	AGE= [("0","<= 18"),
		("1","19-25"),
		("2","26-35"),
		("3","36-45"),
		("4","46-55"),
		("5","56-65"),
		("6",">65"),
		("U","unknown"),
		]
	CHOICE=[
		("E", "E"),
		("F", "F"),
		("M", "M"),
		("U", "U"),
	]
	
	age= models.CharField(max_length=30, null=True, choices=AGE)
	gender= models.CharField(max_length=30, null=True, choices=CHOICE)
	category= models.CharField(max_length=300, null=True, choices=CATEGORY)
	amount= models.FloatField()
	classification= models.CharField(max_length=30, null=True)


	def __str__(self):
		return self.classification