from django.contrib import admin
from djnetaxept.models import NetaxeptPayment, NetaxeptTransaction

admin.site.regiser(NetaxeptPayment)
admin.site.regiser(NetaxeptTransaction)