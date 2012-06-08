from djnetaxept.utils import MERCHANTID, TOKEN

def register(client, req):
    return client.service.Register(
         MERCHANTID,
         TOKEN,
         req
    )
    
def process(client, req):
    return client.service.Process(
         MERCHANTID,
         TOKEN,
         req
    )
    
def query(client, req):
    return client.service.Query(
         MERCHANTID,
         TOKEN,
         req
    )
    
def batch(client, req):
    return client.service.Batch(
         MERCHANTID,
         TOKEN,
         req
    )