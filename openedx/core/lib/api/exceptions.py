"""
Custom exceptions, that allow details to be passed as dict values (which can be
converted to JSON, like other API responses.
"""

from rest_framework import exceptions


class DictAPIException(exceptions.APIException):
    """
    Intermediate class to allow exceptions to pass dict detail values.  Use by
    subclassing this along with another subclass of `exceptions.APIException`.
    """
    def __init__(self, detail):
        if isinstance(detail, dict):
            self.detail = detail
        else:
            super(DictAPIException, self).__init__(detail)


class AuthenticationFailed(exceptions.AuthenticationFailed, DictAPIException):
    """
    Override of DRF's AuthenticationFailed exception to allow dictionary responses.
    """
    pass
