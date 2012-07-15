#!/usr/bin/env python
from djnetaxept.test_utils.cli import configure
import argparse
import os

def main(wsdl, merchantid, token):
    
    configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'djnetaxept.sqlite',
            }
        },
        NETAXEPT_WSDL = wsdl,
        NETAXEPT_MERCHANTID = merchantid,
        NETAXEPT_TOKEN = token
    )
    new_db = not os.path.exists('djnetaxept.sqlite')
    from django.core.management import call_command
    call_command('syncdb', interactive=False, migrate_all=new_db)
    call_command('migrate', interactive=False, fake=new_db)
    call_command('shell')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--wsdl', action='store', dest='wsdl', default='https://epayment-test.bbs.no/netaxept.svc?wsdl')
    parser.add_argument('--merchantid', action='store', dest='merchantid', required=True)
    parser.add_argument('--token', action='store', dest='token', required=True)
    args = parser.parse_args()
    main(args.wsdl, args.merchantid, args.token)