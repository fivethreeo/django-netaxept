from django.db import models
from djnetaxept.managers import NetaxeptPaymentManager, NetaxeptTransactionManager

STATUS_CHOICES = (
    ('AUTHORIZED', 'AUTHORIZED'),
    ('SALE', 'SALE'),
    ('CAPTURE', 'CAPTURE'),
    ('CREDIT', 'CREDIT'),
    ('ANNUL', 'ANNUL')
)

class NetaxeptPayment(models.Model):
    transaction_id = models.CharField(max_length=32)
    amount = models.IntegerField(null=True, blank=True)
    currencycode = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
    ordernumber = models.CharField(max_length=32)
    flagged = models.BooleanField()
    responsecode = models.CharField(max_length=3, null=True, blank=True)
    responsesource = models.CharField(max_length=20, null=True, blank=True)
    responsetext = models.CharField(max_length=255, null=True, blank=True)

    objects = NetaxeptPaymentManager()
    
    def auth(self):
        return NetaxeptTransaction.objects.auth_payment(self)

    def capture(self, amount):
        return NetaxeptTransaction.objects.capture_payment(self, amount)
        
    def credit(self, amount):
        return NetaxeptTransaction.objects.credit_payment(self, amount)
        
    def annul(self):
        return NetaxeptTransaction.objects.annul_payment(self)
    
    def completed(self):
        return not self.flagged
    
"""
RECURRING_CHOICES = (
    ('S', 'S'),
    ('R', 'R')
)
    
class NetaxeptRecurringPayment(NetaxeptPayment):
    recurring_type = models.CharField(max_length=1, choices=RECURRING_CHOICES)
    minimum_frequency = models.PositiveIntegerField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
"""

OPERATION_CHOICES = (
    ('AUTH', 'AUTH'),
    ('SALE', 'SALE'),
    ('CAPTURE', 'CAPTURE'),
    ('CREDIT', 'CREDIT'),
    ('ANNUL', 'ANNUL')
)

class NetaxeptTransaction(models.Model):
    payment = models.ForeignKey(NetaxeptPayment)
    transaction_id = models.CharField(max_length=32)
    operation = models.CharField(max_length=7, choices=OPERATION_CHOICES)
    amount = models.PositiveIntegerField(null=True, blank=True)
    flagged = models.BooleanField()
    responsecode = models.CharField(max_length=3, null=True, blank=True)
    responsesource = models.CharField(max_length=20, null=True, blank=True)
    responsetext = models.CharField(max_length=255, null=True, blank=True)

    objects = NetaxeptTransactionManager()

    def completed(self):
        return not self.flagged