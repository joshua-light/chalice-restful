def config(name):
    def config_body(decorator):
        def decorator_body(value):

            # Validate the value.
            decorator(value)

            def body(*args, **kwargs):
                x = args[0]
                setattr(x, name, value)
                return x

            return body
        return decorator_body
    return config_body


@config(name='authorizer')
def authorized(authorizer):
    """ Wraps a `Resource` subclass or a HTTP-handler function
        and adds `authorizer` field to it, so it'll be able
        to handle authorized requests.
    """
    ...
