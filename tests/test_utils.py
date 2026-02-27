import pytest

from barangay.utils import sanitize_input, _basic_sanitizer


class TestSanitizeInput:
    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("Hello", "hello"),
            ("HELLO", "hello"),
            ("HeLLo WoRLd", "hello world"),
            ("123", "123"),
            ("Test123", "test123"),
            ("", ""),
        ],
    )
    def test_sanitize_input_basic(self, input_str, expected):
        assert sanitize_input(input_str) == expected

    def test_sanitize_input_none(self):
        assert sanitize_input(None) == ""

    def test_sanitize_input_non_string(self):
        assert sanitize_input(123) == ""
        assert sanitize_input([1, 2, 3]) == ""
        assert sanitize_input({"key": "value"}) == ""

    def test_sanitize_input_unicode(self):
        assert sanitize_input("México") == "méxico"
        assert sanitize_input("José") == "josé"
        assert sanitize_input("café") == "café"

    def test_sanitize_input_special_chars(self):
        assert sanitize_input("Hello@World!") == "hello@world!"
        assert sanitize_input("Test#123$") == "test#123$"

    @pytest.mark.parametrize(
        "input_str,exclude,expected",
        [
            ("Hello World", "world", "hello "),
            ("Hello World", ["hello", "world"], " "),
            ("Test.String", ".", "teststring"),
            ("Test-String", "-", "teststring"),
            ("Test,String", ",", "teststring"),
            ("Test(String)", ["(", ")"], "teststring"),
            ("Test&String", "&", "teststring"),
            ("Test(String&Another)", ["(", ")", "&"], "teststringanother"),
        ],
    )
    def test_sanitize_input_with_exclude(self, input_str, exclude, expected):
        assert sanitize_input(input_str, exclude) == expected

    def test_sanitize_input_with_multiple_exclude(self):
        assert sanitize_input("Hello, World.", [",", "."]) == "hello world"
        assert sanitize_input("Test-String_value", ["-", "_"]) == "teststringvalue"

    def test_sanitize_input_exclude_case_insensitive(self):
        assert sanitize_input("HELLO WORLD", "hello") == " world"
        assert sanitize_input("Hello World", ["HELLO", "world"]) == " "

    def test_sanitize_input_empty_string_with_exclude(self):
        assert sanitize_input("", "test") == ""
        assert sanitize_input("", ["a", "b"]) == ""

    def test_sanitize_input_exclude_non_string_in_list(self):
        result = sanitize_input("Hello World", ["hello", 123, None])
        assert result == " world"


class TestBasicSanitizer:
    def test_basic_sanitizer(self):
        assert _basic_sanitizer("Manila") == "manila"

    def test_basic_sanitizer_with_pob(self):
        assert _basic_sanitizer("Manila (pob.)") == "manila "
        assert _basic_sanitizer("Manila (pob)") == "manila "
        assert _basic_sanitizer("Manila pob.") == "manila "

    def test_basic_sanitizer_with_city_of(self):
        assert _basic_sanitizer("City of Manila") == "manila"
        assert _basic_sanitizer("city of Manila") == "manila"

    def test_basic_sanitizer_with_city_suffix(self):
        assert _basic_sanitizer("Manila City") == "manila"
        assert _basic_sanitizer("Quezon city") == "quezon"

    def test_basic_sanitizer_removes_special_chars(self):
        assert _basic_sanitizer("Test.String") == "teststring"
        assert _basic_sanitizer("Test-String") == "teststring"
        assert _basic_sanitizer("Test,String") == "teststring"

    def test_basic_sanitizer_removes_parentheses(self):
        assert _basic_sanitizer("Test(String)") == "teststring"
        assert _basic_sanitizer("Test (String) Value") == "test string value"

    def test_basic_sanitizer_removes_ampersand(self):
        assert _basic_sanitizer("Test&String") == "teststring"
        assert _basic_sanitizer("A&B&C") == "abc"

    def test_basic_sanitizer_complex(self):
        assert _basic_sanitizer("City of Manila (pob.)") == "manila "
        assert _basic_sanitizer("Manila City, Philippines") == "manila philippines"

    def test_basic_sanitizer_empty_string(self):
        assert _basic_sanitizer("") == ""

    def test_basic_sanitizer_none(self):
        assert _basic_sanitizer(None) == ""

    def test_basic_sanitizer_unicode(self):
        assert _basic_sanitizer("México City") == "méxico"
