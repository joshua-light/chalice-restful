from typing import Any


class Ensure:
    """ Represents a bunch of validations,
        which can be applied to a `target`.
    """

    def __init__(self, target: Any):
        self.target = target

    def is_not_a_type(self, x: type):
        """ Checks whether the target type is not equal to the specified.

            :param x: Type compared against `self.target`.
        """

        assert self.target != x, f'Expected {self.target.__name__} ' + \
                                 f'to not be {x.__name__}'


ensure = Ensure
