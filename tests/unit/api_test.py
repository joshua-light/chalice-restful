import pytest
from mock import MagicMock

from chalice_restful import Api, Resource


def test_that_cant_add_resource_class_itself():
    # Arrange.
    api = Api(MagicMock())

    # Act.
    add = lambda: api.add(Resource)

    # Assert.
    with pytest.raises(AssertionError):
        add()


def test_that_cant_add_not_resource_subclass():
    # Arrange.
    class NotResource: ...
    api = Api(MagicMock())

    # Act.
    add = lambda: api.add(NotResource)

    # Assert.
    with pytest.raises(AssertionError):
        add()

# Can't add not `Resource`.
# Can't add resource without `route`.
# Can't add resource without any of `supported_methods` defined.

# `Api.request` should return `chalice.app.current_request`.

# When adding a `Resource`, its routes are added to `Chalice` object.
