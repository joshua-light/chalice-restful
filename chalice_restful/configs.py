from inspect import isclass, isfunction


def _enforce_constraints(decorator, instance):
    enforce_class = getattr(decorator, 'only_classes', False)
    enforce_function = getattr(decorator, 'only_functions', False)

    if enforce_class:
        assert not enforce_function, \
            f'Expected either `only_classes` or `only_functions` flag ' + \
            f'to be set, but not both'
        assert isclass(instance), \
            f'Expected {str(instance)} to be a class'

    if enforce_function:
        assert not enforce_class, \
            f'Expected either `only_classes` or `only_functions` flag ' + \
            f'to be set, but not both'
        assert isfunction(instance), \
            f'Expected {str(instance)} to be a function'


def flag(decorator):
    """ Wraps a decorator that represents a configuration flag. """

    def body(x):

        _enforce_constraints(decorator, x)

        setattr(x, decorator.__name__, True)
        return x

    return body


def config(decorator):
    """ Wraps a decorator that represents some kind of configuration data
        as a named field.
    """

    def decorator_body(value):

        # This allows client to validate the value in decorator body.
        decorator(value)

        def body(*args, **kwargs):

            x = args[0]
            _enforce_constraints(decorator, x)

            setattr(x, decorator.__name__, value)
            return x

        return body
    return decorator_body


@flag
def only_classes():
    """ Adds `only_classes` flag to the decorator function."""


@flag
def only_functions():
    """ Adds `only_functions` flag to the decorator function."""
