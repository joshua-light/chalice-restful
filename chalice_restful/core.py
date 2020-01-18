from chalice import Chalice


class Resource:
    """ Rerpresents a resource or a collection of resources
        which define handlers for `GET`, `POST`, etc. HTTP-calls.

        :examples:
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
        RESTful APIs using resources objects.

        :examples:
             @route('/items')
             class Items:
                 def get(): ...

             app = Chalice()
             api = Api(app)
             api.add(Items)
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
        ...
