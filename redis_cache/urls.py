from django.urls import path, include
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('cookie', get_set_cookie, name='get-set-cookie'),
]