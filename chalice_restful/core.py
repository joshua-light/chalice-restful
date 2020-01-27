from typing import Callable, Dict, Type

from chalice import Chalice
from chalice.app import Request

from chalice_restful.common.guards import ensure
from chalice_restful.configs import config, flag, only_classes


@config
@only_classes
def route(path: str):
    """Adds routing ability to a subclass of `Resource`.

    This decorator is a configuration decorator that only adds
    a `route` attribute to a decorated class and ensures that the `path`
    value represents a valid endpoint.
    """

    ensure(path).starts_with('/')


@flag
def cors():
    """Enables CORS for a decorated endpoint or resource.

    This decorator is a configuration decorator that only adds
    a `cors=True` attribute to a decorated function or class.

    When it's used, the `Api` instance enables Cross-Origin Resource Sharing
    for an endpoint or resource, so one can be requested from another domain.
    """


@flag
def api_key_required():
    """Enforces a decorated endpoint or resource to require API key.

    This decorator is a configuration decorator that only adds
    a `api_key_required=True` attribute to a decorated function or class.

    When it's used, all incoming requests to an endpoint or resource
    should contain a `x-api-key` header with valid key from API Gateway.
    """


class Resource:
    """A resource or a collection of resources.

    Represents a bunch of functions for handling different HTTP-requests.

    Subclasses of this class should define a `route` attribute
    (either directly or using the `route` decorator):
        a) directly:
        class Items:
            route = '/v1/items'
            ...

        b) using the decorator:
        @route('/v1/items')
        class Items:
            ...

    Handlers in the subclasses of the `Resources` are defined as a functions
    with lowercased HTTP-methods names:
        @route('/v1/items')
        class Items:
            def get(): ...  # Will handle GET request.
            def put(): ...  # Will handle PUT request.

    Various configs can be used to enhance the behaviour of the endpoints.
    For example, one could add the `cors` decorator to the `Items` class:
        @route('/v1/items')
        @cors
        class Items:
            def get(): ...
            def put(): ...

    This will make the `get` and `put` endpoints to allow cross domain access.

    On the other hand, it's possible to enable CORS only for specific endpoint:
        @route('/v1/items')
        class Items:
            @cors
            def get(): ...
            def put(): ...
    """


class Api:
    """A RESTful API.

    Represents a collection of `Resource` subclasses, where
    each is able to handle incoming requests.

    The `Api` object should be created using `Chalice` application instance:
        app = Chalice(...)
        api = Api(app)

    Then any number of resources can be defined in the API:
        api.add(Items)
        api.add(Item)
        ...

    All endpoints defined in those resources will be added to the
    `Chalice` instance.

    The `app.app` should be used in the `template.yaml` file as an API handler.
    """

    supported_methods = ['get', 'post', 'put', 'patch', 'delete']

    def __init__(self, app: Chalice):
        self.app = app

    @property
    def request(self) -> Request:
        """Incoming HTTP-request.

        This property is similar to `Chalice.current_request`,
        but is more verbose and small. It's ususally accessed as
        `api.request`.
        """

        return self.app.current_request

    def add(self, resource: Type):
        """Defines a `Resource` in the API.

        All the endpoints defined in the `resource` class that are
        static members will be automatically registered in the
        `Chalice` instance.

        Args:
            resource: Type that rerpresents a group of endpoints.

        Raises:
            AssertionError: Raised if:
                a) `resource` is a `Resource` class itself;
                b) `resource` doesn't have `route` attribute;
                c) `resource` doesn't have endpoints defined.
        """

        def add_method(method: Callable, app: Chalice):
            def put(field: str, to: Dict[str, str]):
                if field not in to:
                    value = getattr(method, field, None) or \
                            getattr(resource, field, None)

                    if value:
                        to[field] = value

            methods = [method.__name__.upper()]
            kwargs = {'methods': methods}

            put('authorizer', to=kwargs)
            put('cors', to=kwargs)
            put('api_key_required', to=kwargs)

            route = app.route(resource.route, **kwargs)
            route(method)

        ensure(resource).is_subclass_of(Resource)
        ensure(resource).has_attribute('route')
        ensure(resource).has_any_attribute(of=self.supported_methods)

        methods = (getattr(resource, x, None) for x in Api.supported_methods)
        methods = [x for x in methods if x]

        for x in methods:
            add_method(x, self.app)
