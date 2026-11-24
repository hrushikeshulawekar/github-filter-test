
from backend.app import add_numbers, greet


def test_add_numbers():
    assert add_numbers(20, 20) == 40


def test_greet():
    assert greet("John") == "Hello, John!"
