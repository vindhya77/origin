from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Videos)
admin.site.register(PharmaDetails)
admin.site.register(PharmaComponents)