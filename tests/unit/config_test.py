from chalice_restful import config, flag


def test_that_config_adds_named_field_to_the_class():
    # Arrange.
    @config(name='field')
    def aspect(_): ...
    class Fake: ...

    # Act.
    Fake = aspect('value')(Fake)

    # Assert.
    assert Fake.field == 'value'


def test_that_config_adds_named_field_to_the_function():
    # Arrange.
    @config(name='field')
    def aspect(_): ...
    def fake(): ...

    # Act.
    fake = aspect('value')(fake)

    # Assert.
    assert fake.field == 'value'


def test_that_flag_adds_named_field_to_the_class():
    # Arrange.
    @flag(name='has_x')
    def has_x(): ...

    # Act.
    @has_x
    class Fake: ...

    # Assert.
    assert Fake.has_x


def test_that_flag_adds_named_field_to_the_function():
    # Arrange.
    @flag(name='has_x')
    def has_x(): ...

    # Act.
    @has_x
    def fake(): ...

    # Assert.
    assert fake.has_x
