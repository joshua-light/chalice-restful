import pytest

from chalice_restful import route


def test_that_route_cant_decorate_not_a_class():
    # Arrange.
    def fake(): ...

    # Act.
    decorate = lambda: route('/')(fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()


def test_that_route_adds_route_field_to_the_class():
    # Arrange.
    class Fake: ...

    # Act.
    Fake = route('/')(Fake)

    # Assert.
    assert Fake.route == '/'
