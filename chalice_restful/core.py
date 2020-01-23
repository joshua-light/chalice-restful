from chalice import Chalice

from chalice_restful.common.guards import ensure
from chalice_restful.configs import flag


def route(path: str):
    """ Wraps a `Resource` subclass and adds a `route` field to it,
        so it'll be able to handle incoming requests.
    """

    ensure(path).starts_with('/')

    def body(cls):
        ensure(cls).is_class()

        cls.route = path

        return cls
    return body


@flag
def cors():
    """ Wraps a `Resource` subclass or a HTTP-handler function
        and adds `cors` field to it, so it'll be able
        to handle CORS.
    """


class Resource:
    """ Rerpresents a resource or a collection of resources
        which define handlers for `GET`, `POST`, etc. HTTP-calls.

        :examples:
            @route('v1/items)
            class Items:
                def get(): ...
                def put(): ...
                def post(): ...
                def patch(): ...
                def delete(): ...
    """
    ...


class Api:
    """ Represents an API that contains routed resources. """

    supported_methods = ['get', 'post', 'put', 'patch', 'delete']

    def __init__(self, app: Chalice):
        self.app = app

    @property
    def request(self):
        """ Incoming HTTP-request. """

        return self.app.current_request

    def add(self, resource: type) -> 'Api':
        """ Defines a `Resource` in the API.

            :param resource: Type that rerpresents a group of endpoints.
            :return: `self` object.
            :remarks: Resources that were added to the API
                      should be decorated with `route` to ensure
                      they're able to handle incoming requests.
        """

        def add_method(method: callable, app: Chalice):
            def put(field: str, to: dict):
                if field not in to:
                    value = getattr(method, field, None) or \
                            getattr(resource, field, None)

                    if value:
                        to[field] = value

            methods = [method.__name__.upper()]
            kwargs = {'methods': methods}

            put('authorizer', to=kwargs)

            route = app.route(resource.route, **kwargs)
            route(method)

        ensure(resource).is_subclass_of(Resource)
        ensure(resource).has_attribute('route')
        ensure(resource).has_any_attribute(of=self.supported_methods)

        methods = (getattr(resource, x, None) for x in Api.supported_methods)
        methods = [x for x in methods if x]

        for x in methods:
            add_method(x, self.app)
