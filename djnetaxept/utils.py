# -*- coding: utf-8 -*-
from django.conf import settings
from suds.client import Client

import logging
logger = logging.getLogger(__name__)

WSDL = getattr(settings, 'NETAXEPT_WSDL', 'https://epayment-test.bbs.no/netaxept.svc?wsdl')
MERCHANTID = getattr(settings, 'NETAXEPT_MERCHANTID', '')
TOKEN = getattr(settings, 'NETAXEPT_TOKEN', '')
TERMNAL = getattr(settings, 'NETAXEPT_TERMINAL', 'https://epayment-test.bbs.no/Terminal/default.aspx')
CURRENCY_CODE = getattr(settings, 'NETAXEPT_CURRENCY_CODE', 'NOK')

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
    environment.WebServicePlatform = 'SUDS' 
    
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
    logger.debug(exception.fault)
    bbsexception = getattr(exception.fault.detail, 'BBSException', None)
    obj.flagged = True
    if bbsexception:
        result = bbsexception.Result
        obj.responsecode = str(result.ResponseCode)
        obj.responsesource = result.ResponseSource
        obj.responsetext = result.ResponseText
        obj.message = bbsexception.Message
    else:
        obj.responsetext = exception.fault.detail[0].Message

