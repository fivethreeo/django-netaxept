from django.contrib import admin
from djnetaxept.models import NetaxeptPayment, NetaxeptTransaction

admin.site.register(NetaxeptPayment)
admin.site.register(NetaxeptTransaction)