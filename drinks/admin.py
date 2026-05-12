#just to show it on the admin page(optional)
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)