from chalice.app import Authorizer

from chalice_restful import config


@config
def authorizer(_: Authorizer):
    """Adds an authorizer to an endpoint or a resource.

    Instance of the authorizer is responsible for
    authorization and should be of type `chalice.app.Authorizer`.

    Read more: https://github.com/aws/chalice/blob/master/docs/source/topics/authorizers.rst.
    """
