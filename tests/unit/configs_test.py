import pytest

from chalice_restful import config, flag, only_classes, only_functions


def test_that_config_adds_named_field_to_the_class():
    # Arrange.
    @config
    def aspect(_): ...
    class Fake: ...

    # Act.
    Fake = aspect('value')(Fake)

    # Assert.
    assert Fake.aspect == 'value'


def test_that_config_adds_named_field_to_the_function():
    # Arrange.
    @config
    def aspect(_): ...
    def fake(): ...

    # Act.
    fake = aspect('value')(fake)

    # Assert.
    assert fake.aspect == 'value'


def test_that_flag_adds_named_field_to_the_class():
    # Arrange.
    @flag
    def has_x(): ...

    # Act.
    @has_x
    class Fake: ...

    # Assert.
    assert Fake.has_x


def test_that_flag_adds_named_field_to_the_function():
    # Arrange.
    @flag
    def has_x(): ...

    # Act.
    @has_x
    def fake(): ...

    # Assert.
    assert fake.has_x


def test_that_only_classes_flag_cant_be_added_to_function():
    # Arrange.
    @flag
    @only_classes
    def has_x(): ...

    def fake(): ...

    # Act.
    decorate = lambda: has_x(fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()


def test_that_only_functions_flag_cant_be_added_to_class():
    # Arrange.
    @flag
    @only_functions
    def has_x(): ...

    class Fake: ...

    # Act.
    decorate = lambda: has_x(Fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()


def test_that_only_classes_config_cant_be_added_to_function():
    # Arrange.
    @config
    @only_classes
    def has_x(): ...

    def fake(): ...

    # Act.
    decorate = lambda: has_x('value')(fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()


def test_that_only_functions_config_cant_be_added_to_class():
    # Arrange.
    @config
    @only_functions
    def has_x(): ...

    class Fake: ...

    # Act.
    decorate = lambda: has_x('value')(Fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()


def test_that_cant_add_both_only_functions_and_only_classes_flags_to_class():
    # Arrange.
    @config
    @only_functions
    @only_classes
    def has_x(): ...

    class Fake: ...

    # Act.
    decorate = lambda: has_x('value')(Fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()


def test_that_cant_add_both_only_functions_and_only_classes_flags_to_function():
    # Arrange.
    @config
    @only_functions
    @only_classes
    def has_x(): ...

    def fake(): ...

    # Act.
    decorate = lambda: has_x('value')(fake)

    # Assert.
    with pytest.raises(AssertionError):
        decorate()
