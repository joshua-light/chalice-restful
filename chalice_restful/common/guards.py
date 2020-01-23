from typing import Any, Iterable
from inspect import isclass


class Ensure:
    """ Represents a bunch of validations,
        which can be applied to the `target`.
    """

    def __init__(self, target: Any):
        self.target = target

    def is_class(self):
        """ Ensures that the target is a class. """

        assert isclass(self.target), \
            f'Expected {self.target} ' + \
            f'to be a class'

    def is_not(self, x):
        """ Ensures that the target is not equal to the specified value. """

        assert self.target != x, \
            f'Expected {self.target} ' + \
            f'to not be {x}'

    def is_subclass_of(self, x: type):
        """ Ensures that the target type is subclass of the specified. """

        assert issubclass(self.target, x), \
            f'Expected {self.target} ' + \
            f'to be a subclass of {x}'

    def has_attribute(self, attribute: str):
        """ Ensures that the target type has attribute
            of the specified name.
        """

        assert hasattr(self.target, attribute), \
            f'Expected {self.target} ' + \
            f'to have a {attribute} attribute'

    def has_any_attribute(self, of: Iterable[str]):
        """ Ensures that the target type has any
            of the specified attributes.
        """

        matched = (getattr(self.target, x, None) for x in of)

        assert any(matched), \
            f'Expected {self.target} to define at least one ' + \
            f'of the {of} attributes'

    def starts_with(self, prefix: str):
        """ Ensures that the target string starts with
            the specified prefix.
        """

        assert self.target.startswith(prefix), \
            f'Expected {self.target} to start with {prefix}'


ensure = Ensure
