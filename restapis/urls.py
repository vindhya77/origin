from django.urls import path, include
from .views import *

urlpatterns = [
	path('api-view', home, name='home'),
	path('post', post_data, name='post_data'),
	path('update/<int:id>/', update_data, name='update_data'),
]