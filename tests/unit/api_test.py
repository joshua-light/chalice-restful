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


def test_that_cant_add_resource_without_route_field():
    # Arrange.
    class NonDecoratedResource(Resource): ...
    api = Api(MagicMock())

    # Act.
    add = lambda: api.add(NonDecoratedResource)

    # Assert.
    with pytest.raises(AssertionError):
        add()


def test_that_cant_add_resource_without_supported_methods():
    # Arrange.
    class SimpleResource(Resource):
        route = '/'

    api = Api(MagicMock())

    # Act.
    add = lambda: api.add(SimpleResource)

    # Assert.
    with pytest.raises(AssertionError):
        add()


def test_that_when_adding_resource_its_endpoints_are_added_to_chalice():
    # Arrange.
    class SimpleResource(Resource):
        route = '/'

        def get(): ...

    app = MagicMock()
    route = MagicMock()
    app.route = MagicMock(return_value=route)
    api = Api(app)

    # Act.
    api.add(SimpleResource)

    # Assert.
    app.route.assert_called_with('/', methods=['GET'])
    route.assert_called_with(SimpleResource.get)


# `Api.request` should return `chalice.app.current_request`.
