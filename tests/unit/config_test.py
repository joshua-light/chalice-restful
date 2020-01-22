import pytest

from chalice_restful import config


def test_that_config_adds_named_field_to_the_class():
    # Arrange.
    @config(name='field')
    def aspect(_): ...
    class Fake: ...

    # Act.
    Fake = aspect('value')(Fake)

    # Assert.
    assert Fake.field == 'value'
