# spicy_ids/tests/test_generate_random_strings.py

from pytest import raises
from typing import Any

from src.generate_random_strings import generate_random_string


def test_generate_strings() -> None:
    LENGTH: int = 10
    result: Any = generate_random_string(length=LENGTH)
    assert isinstance(result, str)


def test_check_length_of_string() -> None:
    LENGTH: int = 10
    result: Any = generate_random_string(length=LENGTH)
    assert len(result) == LENGTH


def test_check_for_wrong_parameter() -> None:
    LENGTH: str = "abc"
    with raises(TypeError) as e_info:
        result: Any = generate_random_string(length=LENGTH)


def test_check_for_none_call() -> None:
    LENGTH: None = None
    with raises(SyntaxError) as e_info:
        result: Any = generate_random_string(length=LENGTH)


def test_check_for_empty_call() -> None:
    result: Any = generate_random_string()
    assert result is not None
    assert len(result) == 15

