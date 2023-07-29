"""Allow for practice of cards.

This could be random practice. 
Practice the 

"""
from typing import List

import numpy as np


def random_order(cards: List, seed=None) -> List:
    """Return a random order of the cards."""
    if seed is not None:
        np.random.seed(seed)

    return np.random.permutation(cards)


def same_order(cards: List) -> List:
    """Return the cards in the same order."""
    return cards


def most_recent(cards: List) -> List:
    """Return the cards in the order of most recent."""
    raise NotImplementedError("This is not implemented yet.")


available_practice_types = {
    "random": random_order,
    "same": same_order,
    "most-recent": most_recent,
}
