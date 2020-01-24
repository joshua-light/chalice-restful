# Chalice-RESTful

A more structured way of writing [Chalice](https://github.com/aws/chalice) APIs.
Very similar to [Flask-RESTful](https://github.com/flask-restful/flask-restful).

## Motivation

In pure [Chalice](https://github.com/aws/chalice) you only need to define plain functions
that handle routed HTTP-requests:

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
def add_orders(): ...
```

It'd be much better if we could use an object-oriented approach, so closely related functions
will be grouped together in a class.

An this is _exactly_ what the Chalice-RESTful for:

``` python
app = Chalice('example')
api = Api(app)

@route('/v1/items')
class Items(Resource):
    def get(): ...
    def post(): ...

@route('/v1/orders)
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

It's worth mentioning that you can use configuration attribute `route` that will add
`route` attribute automatically while preserving pretty decorators syntax:

``` python
from chalice_restful import Api, Resource, route

app = Chalice('example')
api = Api(app)

@route('/v1/items')
class Items(Resource):
    def get(): ...

api.add(Items)
```

### Authorization

...

#### API key

...

#### Authorizers

...

### CORS

...

## License

The package is licensed under the [MIT](https://github.com/JoshuaLight/chalice-restul/blob/master/LICENSE) license.
