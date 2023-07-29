import numpy as np

from cards.practice import random_order, same_order


def test_random_order():
    cards = ["a", "b", "c"]
    np.testing.assert_array_equal(random_order(cards, seed=0), ["c", "b", "a"])


def test_same_order():
    cards = ["a", "b", "c"]
    np.testing.assert_array_equal(same_order(cards), ["a", "b", "c"])
