import pytest

from cards.guess import exactly_correct, approximately_correct


@pytest.mark.parametrize(
    "guess, answer",
    [
        ("Hello", "Hello"),
        ("Hello", "hello"),
        ("Hello", "hello "),
        ("hello", "   hello "),
    ],
)
def test_exactly_correct(guess, answer):
    assert exactly_correct(guess, answer)
