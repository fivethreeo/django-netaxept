class BaseNetaxeptException(Exception):
    def __str__(self):
        return repr(self.msg)

class PaymentNotAuthorized(BaseNetaxeptException):
    msg = 'Payment not authorized'

class AmountAllreadyCaptured(BaseNetaxeptException):
    msg = 'Amount allready captured, do a CREDIT'

class NoAmountCaptured(BaseNetaxeptException):
    msg = 'No amount captured nothing to CREDIT'