from chalice import Chalice

from chalice_restful.guards import ensure


def route(path: str):
    """ Wraps a `Resource` subclass and adds a `route` field to it,
        so it'll be able to handle incoming requests.
    """
    ...


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
    """ Represents an API object that allows developers to define
        RESTful APIs using routed objects.
    """

    supported_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    def __init__(self, app: Chalice):
        self.app = app

    @property
    def request(self):
        """ Incoming HTTP-request. """
        ...

    def add(self, resource: type) -> 'Api':
        """ Defines a `Resource` in the API.

            :param resource: Type that rerpresents a group of endpoints.
            :return: `self` object.
            :remarks: Resources that were added to the API
                      should be decorated with `route` to ensure
                      they're able to handle incoming requests.
        """

        ensure(resource).is_not_a_type(Resource)
        ensure(resource).is_subclass_of(Resource)
        ensure(resource).has_attribute('route')
