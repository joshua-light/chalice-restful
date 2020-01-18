from typing import Any, Iterable


class Ensure:
    """ Represents a bunch of validations,
        which can be applied to a `target`.
    """

    def __init__(self, target: Any):
        self.target = target

    def is_not(self, x: type):
        """ Checks whether the target is not equal to the specified value. """

        assert self.target != x, \
            f'Expected {str(self.target)} ' + \
            f'to not be {str(x)}'

    def is_subclass_of(self, x: type):
        """ Checks whether the target type is subclass of the specified. """

        assert issubclass(self.target, x), \
            f'Expected {str(self.target)} ' + \
            f'to be a subclass of {str(x)}'

    def has_attribute(self, attribute: str):
        """ Checks whether the target type has attribute
            of the specified name.
        """

        assert hasattr(self.target, attribute), \
            f'Expected {str(self.target)} ' + \
            f'to have a {attribute} attribute.'

    def has_any_attribute(self, of: Iterable[str]):
        """ Checks whether the target type has any
            of the specified attributes.
        """

        matched = (getattr(self.target, x, None) for x in of)

        assert any(matched), \
            f'Expected {str(self.target)} to define at least one ' + \
            f'of the {of} attributes.'


ensure = Ensure
