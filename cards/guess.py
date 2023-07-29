def exactly_correct(guess: str, answer: str) -> bool:
    return guess.strip().lower() == answer.strip().lower()


def approximately_correct(guess: str, answer: str) -> bool:
    return guess.strip().lower() in answer.strip().lower()
