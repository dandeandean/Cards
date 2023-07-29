from sqlmodel import Session

from cards.db import get_engine, Card, Category


if __name__ == "__main__":
    engine = get_engine()

    session = Session(engine)

    with Session(engine) as session:
        german = Category(name="German")
        basic_german = Category(name="Basic German")
        french = Category(name="French")
        stats = Category(name="Statistics")

        cards = [
            Card(front="hello", back="hallo", categories=[german, basic_german]),
            Card(front="goodbye", back="Auf Wiedersehen", categories=[german, basic_german]),
            Card(front="goodbye", back="au revoir", categories=[french]),
            Card(front="P[A | B]", back="P[B | A] * P[A] / P[B]", categories=[stats]),

        ]
        for card in cards:
            session.add(card)

        session.commit()