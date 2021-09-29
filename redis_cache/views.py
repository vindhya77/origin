from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from .models import *


def home(request):
	payload = []
	db = None

	if cache.get('friuts'):
		db = 'redis'
		payload = cache.get('friuts')
	else:
		friuts = Fruit.objects.all()
		for friut in friuts:
			payload.append(friut.name)
		db = 'sqlite'

		cache.set('friuts', payload)

	return JsonResponse({'status': 200, 'db': db, 'data': payload})


def get_set_cookie(request):  
	if request.COOKIES.get('loggedIn'):
		html = HttpResponse("<center>Already logged user<br>{0}</center>".format(request.COOKIES['loggedIn']))
	else:
		html = HttpResponse("<h1>Welcome to Django Website</h1>")
		html.set_cookie('loggedIn', 'Yes', max_age = None)

	return html 

	
