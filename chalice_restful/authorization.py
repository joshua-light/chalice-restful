from chalice_restful import config


@config
def authorizer(_):
    """Adds authorizer to an endpoint or a resource.
        and adds `authorizer` field to it, so it'll be able
        to handle authorized requests.
    """
