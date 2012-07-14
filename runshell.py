#!/usr/bin/env python
from shop_example.test_utils.cli import configure

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
    from django.core.management import call_command
    call_command('shell')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--wsdl', action='store', dest='wsdl')
    parser.add_argument('--merchantid', action='store', dest='merchantid')
    parser.add_argument('--token', action='store', dest='token')
    args = parser.parse_args()
    main(args.wsdl, args.merchantid, args.token)