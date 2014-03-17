from django.db import models

class Environment(models.Model):
	name		= models.CharField(max_length = 50)

class User(models.Model):
	mail 		= models.EmailField()
	password 	= models.CharField(max_length = 50)
	name 		= models.CharField(max_length = 50)
	photo		= models.CharField(max_length = 50)
	environment	= models.ManyToManyField(Environment)

class Expenditure(models.Model):
	date 		= models.DateTimeField(auto_now = True)
	amount		= models.DecimalField(max_digits = 12, decimal_places = 2)
	description 	= models.CharField(max_length = 200)
	where		= models.CharField(max_length = 50)
	name		= models.CharField(max_length = 50)
	environment	= models.ForeignKey('Environment')
	user		= models.ManyToManyField(User)

class Product(models.Model):
	amount		= models.DecimalField(max_digits = 12, decimal_places = 2)
	quantity	= models.IntegerField()
	name		= models.CharField(max_length = 50)
	expenditure	= models.ForeignKey('Expenditure')
	user		= models.ManyToManyField(User)


