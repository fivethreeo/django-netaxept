# -*- coding: utf-8 -*-

from suds.client import Client

from django.conf import settings

WSDL = getattr(settings, 'NETAXEPT_WSDL', 'https://epayment-test.bbs.no/netaxept.svc?wsdl')
MERCHANTID = getattr(settings, 'NETAXEPT_MERCHANTID', '')
TOKEN = getattr(settings, 'NETAXEPT_TOKEN', '')

AUTOAUTH = getattr(settings, 'NETAXEPT_AUTOAUTH', None)
PAYMENT_METHOD_LIST = getattr(settings, 'NETAXEPT_PAYMENT_METHOD_LIST', None)
PAYMENT_FEE_LIST = getattr(settings, 'NETAXEPT_PAYMENT_FEE_LIST', None)

def get_client():        
    return Client(WSDL, faults=True)
    
def get_netaxept_object(client, obj):
    return client.factory.create('ns1:%s' % obj)
    
def get_basic_registerrequest(client, redirecturl, language):
    # return a basic registerrequestuest without order
    environment = get_netaxept_object(client, 'Environment')
    environment.Language = None
    environment.OS = None
    environment.WebServicePlatform = 'ZSI' 
    
    terminal = order = get_netaxept_object(client, 'Terminal')
    terminal.AutoAuth = AUTOAUTH
    terminal.PaymentMethodList = PAYMENT_METHOD_LIST
    terminal.FeeList = PAYMENT_FEE_LIST
    terminal.Language = language
    terminal.OrderDescription = None
    terminal.RedirectOnError = None
    terminal.RedirectUrl = redirecturl
    
    request = order = get_netaxept_object(client, 'RegisterRequest')
    request.AvtaleGiro = None
    request.CardInfo = None
    request.Customer = None
    request.DnBNorDirectPayment = None
    request.Environment = environment
    request.ServiceType = None
    request.Terminal = terminal
    request.Recurring = None

    return request
        
def handle_response_exception(exception, obj):
    fault = exception.fault.detail[0]
    obj.flagged = True
    obj.responsecode = getattr(fault, 'ResponseCode', None)
    obj.responsesource = getattr(fault, 'ResponseSource', None)
    text = getattr(fault, 'ResponseText', None)
    if not text:
        text = getattr(fault, 'Message', None)
    obj.responsetext = text