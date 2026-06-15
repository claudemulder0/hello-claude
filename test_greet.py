"""Tests for greet.py."""

from greet import greet


def test_greet_default():
    result = greet("World")
    assert "Hello, World!" in result


def test_greet_custom_name():
    result = greet("Alice")
    assert "Hello, Alice!" in result


def test_greet_includes_timestamp():
    result = greet("Bob")
    # Timestamp format is [HH:MM]
    assert result.startswith("[")
    assert "]" in result
