from django.urls import path

from .rest_framework_views import PharmaDetailView


app_name = "restapi"

urlpatterns = [
    path('details/', PharmaDetailView.as_view()),
]