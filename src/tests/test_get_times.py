# spicy_ids/tests/test_get_times.py

from pytest import raises
from typing import Any

from spicyid.generate_timestamp_value import (
    get_unix_time,
    mask_timestamp,
    get_masked_ts,
)


# get_unix_time tests
def test_get_unix_time() -> None:
    result: Any = get_unix_time()
    assert isinstance(result, int)


def test_get_unix_time_with_parameter() -> None:
    with raises(TypeError) as e_info:
        result: Any = get_unix_time(time="today")


# mask_timestamp tests
def test_mask_timestamp() -> None:
    TIMESTAMP_TEST_VAL: int = get_unix_time()
    result: Any = mask_timestamp(ts=TIMESTAMP_TEST_VAL)
    assert isinstance(result, str)


def test_mask_timestamp_wrong_argument() -> None:
    TIMESTAMP_TEST_VAL: str = "the current time is now"
    with raises(TypeError) as e_info:
        result: Any = mask_timestamp(ts=TIMESTAMP_TEST_VAL)


def test_mask_timestamp_no_argument() -> None:
    with raises(TypeError) as e_info:
        result: Any = mask_timestamp()


# get_masked_ts tests
def test_get_masked_ts() -> None:
    result: Any = get_masked_ts()
    assert isinstance(result, str)


def test_gest_masked_ts_with_argument() -> None:
    ARGUMENT_TEST_VAL: str = "now"
    with raises(TypeError) as e_info:
        result: Any = get_masked_ts(ts=ARGUMENT_TEST_VAL)
