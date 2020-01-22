import pytest

from chalice_restful import authorized


def test_that_authorized_adds_authorizer_field_to_the_class():
    # Arrange.
    class Fake: ...

    # Act.
    Fake = authorized('')(Fake)

    # Assert.
    assert Fake.authorizer == ''
