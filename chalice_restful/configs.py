from inspect import isclass, isfunction
from typing import Any, Callable


def _enforce_constraints(decorator: Callable, instance: Any):
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


def flag(decorator: Callable):
    """Makes another decorator a flag.

    `flag` is a high level decorator that should be
    applied on decorators:
        @flag
        def enabled(): ...

    Here the `enabled` decorator can be considered as a flag,
    so when applied it'll add an `enabled` attribute with a value of `True`
    to the target instance.

    For example:
        @enabled
        def func(): ...

        print(func.enabled)  # Prints `True`.

    Classes can be decorated as well:
        @enabled
        class Test: ...

        print(Test.enabled)  # Prints `True`.
    """

    def body(x: Any):

        _enforce_constraints(decorator, x)

        setattr(x, decorator.__name__, True)
        return x

    return body


def config(decorator: Callable):
    """Makes another decorator a config.

    `config` is a high level decorator that should be
    applied on decorators:
        @config
        def speed(value): ...

    Decorators `config` is applied on must accept one
    argument that represents a value of config. This also
    affects how those decorators are applied:
        @speed(100)
        def func(): ...

        print(func.speed)  # Prints `100`.

    Here, when applied, `speed` decorator adds `speed` attribute
    to the target instance that is equal to `100`.

    Classes can be decorated as well:
        @speed(100)
        class Test: ...

        print(Test.speed)  # Prints `100`.

    It's possible to validate the input right in the body of the decorator:
        @config
        def speed(value):
            assert value >= 0
    """

    def decorator_body(value: Any):

        # This allows client to validate the value in the decorator body.
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
    """Makes configuration decorator applicable only on classes.

    This decorator works as a `flag`, so it adds the `only_classes`
    boolean attribute to the decorated object. This allows
    the `flag` or the `config` decorators to ensure that
    decorated object is a class, but not a function.

    For example:
        @flag
        @only_classes
        def enabled(): ...

        @enabled
        class Test: ...  # Valid.

        @enabled
        def test(): ...  # Invalid.

    It's impotant to place `only_classes` BELOW `flag` or `config`,
    so the added `only_classes` attribute is visible above.

    This example is invalid:
        @only_classes  # Should be below.
        @flag
        def enabled(): ...
    """


@flag
def only_functions():
    """Makes configuration decorator applicable only on functions.

    This decorator works as a `flag`, so it adds the `only_functions`
    boolean attribute to the decorated object. This allows
    the `flag` or the `config` decorators to ensure that
    decorated object is a function, but not a class.

    For example:
        @flag
        @only_functions
        def enabled(): ...

        @enabled
        def test(): ...  # Valid.

        @enabled
        class Test: ...  # Invalid.


    It's impotant to place `only_functions` BELOW `flag` or `config`,
    so the added `only_functions` attribute is visible above.

    This example is invalid:
        @only_functions  # Should be below.
        @flag
        def enabled(): ...
    """
