from chalice_restful import config


@config(name='authorizer')
def authorized(_):
    """ Wraps a `Resource` subclass or a HTTP-handler function
        and adds `authorizer` field to it, so it'll be able
        to handle authorized requests.
    """
