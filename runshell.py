#!/usr/bin/env python
from djeasytests.testsetup import TestSetup, default_settings

class NetaxeptTestSetup(TestSetup):
        
    def get_argparser(self):
        parser = super(NetaxeptTestSetup, self).get_argparser()
        parser.add_argument('--wsdl', action='store', dest='wsdl', default='https://epayment-test.bbs.no/netaxept.svc?wsdl')
        parser.add_argument('--merchantid', action='store', dest='merchantid', required=True)
        parser.add_argument('--token', action='store', dest='token', required=True)
        return parser
        
    def handle_args(self, args):
        return dict(
            NETAXEPT_WSDL = args.wsdl,
            NETAXEPT_MERCHANTID = args.merchantid,
            NETAXEPT_TOKEN = args.token
        )

default_settings.update(dict(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'djnetaxept.sqlite',
        }
    }
))

testsetup = NetaxeptTestSetup(appname='djnetaxept', default_settings=default_settings)

if __name__ == '__main__':
    testsetup.run('shell')