import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
      ("python", "Python"),
      ("Skypro", "Skypro"),
      ("hello world", "Hello world"),
      ("123test", "123test"),
      ("04 апреля 2025", "04 апреля 2025"),
      ("@skypro", "@skypro"),
    ]
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
      ("", ""),
      ("  ", "  "),
    ]
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
      ("   test", "test"),
      (" test", "test"),
      ("skypro", "skypro"),
      ("  123 test ", "123 test "),
      ("     f", "f"),
    ]
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
      ("", ""),
      ("   ", ""),
    ]
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize(
    ("string", "symbol", "expected"),
    [
      ("test", "t", True),
      ("test", "f", False),
      ("", "a", False),
      (" ", " ", True),
      ("hello", "", True),
    ]
)
def test_contains_param(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    ("string", "symbol", "expected"),
    [
      ("skypro", "s", "kypro"),
      ("sssss", "s", ""),
      ("SkyPro", "s", "SkyPro"),
      ("04 апреля 2025", " ", "04апреля2025"),
    ]
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    ("string", "symbol", "expected"),
    [
      ("pro", "qwe", "pro"),
      ("", "f", ""),
      ("   ", " ", ""),
      ("aaa", "aa", "a"),
    ]
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.xfail(raises=AttributeError, reason="Метод не обрабатывает None")
def test_delete_symbol_none_string():
    string_utils.delete_symbol(None, "a")
