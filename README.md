# Chalice-RESTful

[![Build](https://github.com/JoshuaLight/chalice-restful/workflows/Build/badge.svg)](https://github.com/JoshuaLight/chalice-restful/actions)
[![PyPI version](https://badge.fury.io/py/chalice-restful.svg)](https://badge.fury.io/py/chalice-restful)

_A more structured way of writing [Chalice](https://github.com/aws/chalice) APIs.
Very similar to [Flask-RESTful](https://github.com/flask-restful/flask-restful)._

## Motivation

In pure [Chalice](https://github.com/aws/chalice) you only need to define plain functions
to handle routed HTTP-requests:

``` python
app = Chalice('example')

@app.route('/v1/items', methods=['GET'])
def get_items(): ...

@app.route('/v1/items', methods=['POST'])
def add_item(): ...
```

This is great for building any kind of API, but in REST we deal with
higher level objects -- resources, where each represents a set of functions
related to each other.

Though we still limited to write them in one place:

``` python
app = Chalice('example')

@app.route('/v1/items', methods=['GET'])
def get_items(): ...

@app.route('/v1/items', methods=['POST'])
def add_item(): ...

...

@app.route('/v1/orders', methods=['GET'])
def get_orders(): ...

@app.route('/v1/orders', methods=['POST'])
def add_order(): ...
```

It'd be much better if we could use an object-oriented approach, so closely related functions
will be grouped together in a class.

And this is _exactly_ what the Chalice-RESTful for:

``` python
app = Chalice('example')
api = Api(app)

@route('/v1/items')
class Items(Resource):
    def get(): ...
    def post(): ...

@route('/v1/orders')
class Orders(Resource):
    def get(): ...
    def post(): ...

api.add(Items)
api.add(Orders)
```

## Installation

Install Chalice-RESTful with `pip`:

``` shell
$ pip install chalice-restful
```

## Usage

### Resources

An atomic block of Chalice-RESTful is a _resource_: any subclass of the `Resource`
that has `route` attribute and at least one endpoint (`get`, `post`, `put`, etc.).
All resources should be then added to the `Api` object that will take care of registering
each individual endpoint in the `Chalice` instance.

``` python
from chalice import Chalice
from chalice_restful import Api, Resource

app = Chalice('example')
api = Api(app)

class Items(Resource):
    route = '/v1/items'

    def get(): ...

api.add(Items)
```

It's worth mentioning that you can use configuration decorator `route` that will add
`route` attribute automatically while preserving pretty decorators syntax:

``` python
from chalice import Chalice
from chalice_restful import Api, Resource, route

app = Chalice('example')
api = Api(app)

@route('/v1/items')
class Items(Resource):
    def get(): ...

api.add(Items)
```

#### HTTP Methods

Currently, Chalice-RESTful supports `get`, `post`, `put`, `patch` and `delete` endpoints,
which can be defined in resources.

### Authorization

You can add an authorization to resources or endpoints in several ways.

#### API key

To require an API key use `api_key_required` configuration decorator:

``` python
from chalice import Chalice
from chalice_restful import Api, Resource, api_key_required, route

app = Chalice('example')
api = Api(app)

@route('/v1/items')
@api_key_required
class Items(Resource):
    def get(): ...

api.add(Items)
```

You can decorate individual endpoints as well:

``` python
from chalice import Chalice
from chalice_restful import Api, Resource, api_key_required, route

app = Chalice('example')
api = Api(app)

@route('/v1/items')
class Items(Resource):
    def get(): ...

    @api_key_required
    def post(): ...

    @api_key_required
    def put(): ...

api.add(Items)
```

#### Authorizers

To add an authorizer instance use `authorizer` configuration decorator:

``` python
from chalice import Chalice, IAMAuthorizer
from chalice_restful import Api, Resource, authorizer, route

app = Chalice('example')
api = Api(app)
iam = IAMAuthorizer()

@route('/v1/items')
@authorizer(iam)
class Items(Resource):
    def get(): ...

api.add(Items)
```

You can decorate individual endpoints as well:

``` python
from chalice import Chalice, IAMAuthorizer
from chalice_restful import Api, Resource, authorizer, route

app = Chalice('example')
api = Api(app)
iam = IAMAuthorizer()

@route('/v1/items')
class Items(Resource):
    def get(): ...

    @authorizer(iam)
    def post(): ...

    @authorizer(iam)
    def put(): ...

api.add(Items)
```

Read more about Chalice authorizers [here](https://github.com/aws/chalice/blob/master/docs/source/topics/authorizers.rst).

### CORS

To enable CORS use `cors` configuration decorator:

``` python
from chalice import Chalice
from chalice_restful import Api, Resource, cors, route

app = Chalice('example')
api = Api(app)

@route('/v1/items')
@cors
class Items(Resource):
    def get(): ...

api.add(Items)
```

You can decorate individual endpoints as well:
``` python
from chalice import Chalice
from chalice_restful import Api, Resource, cors, route

app = Chalice('example')
api = Api(app)

@route('/v1/items')
class Items(Resource):
    def get(): ...

    @cors
    def post(): ...

    @cors
    def put(): ...


api.add(Items)
```

## License

The package is licensed under the [MIT](https://github.com/JoshuaLight/chalice-restul/blob/master/LICENSE) license.
