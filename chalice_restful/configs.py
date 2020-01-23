def flag(decorator):
    """ Wraps a decorator that represents a configuration flag. """

    def body(x):

        setattr(x, decorator.__name__, True)
        return x

    return body


def config(decorator):
    """ Wraps a decorator that represents some kind of configuration data
         as a named field.
    """

    def decorator_body(value):
        def body(*args, **kwargs):

            x = args[0]
            setattr(x, decorator.__name__, value)
            return x

        return body
    return decorator_body
