import typer

from rich.console import Console
from rich.prompt import Prompt, IntPrompt

from sqlmodel import Session, select

from cards.db import (
    get_engine,
    Category,
    Card,
    PracticeSession,
    PracticeHistory,
    PracticeType,
)
from cards.guess import exactly_correct
from cards.practice import available_practice_types


app = typer.Typer()
console = Console()


@app.command()
def new_card():
    """Create a new card."""
    console.print("Creating a new card...")
    name = console.input("category: ")
    front = console.input("front: ")
    back = console.input("back: ")

    engine = get_engine()
    with Session(engine) as session:
        category = session.exec(select(Category).where(Category.name == name)).first()

        if category is None:
            category = Category(name=name)

        card = Card(front=front, back=back, categories=[category])
        session.add(card)
        session.commit()

        session.refresh(card)

    console.print(f"[green]Created card: {card}[/green]")


@app.command()
def ls():
    """List cards in a category."""
    console.print("ls")
    desired_category = console.input("category: ")

    engine = get_engine()
    with Session(engine) as session:
        result = session.exec(
            select(Category).where(Category.name == desired_category)
        ).first()

        if result is None:
            console.print(f"[red]No category named {desired_category}[/red]")
            return

        for card in result.cards:
            console.print(card)


def list_all_from_table(engine, model, name: str):
    with Session(engine) as session:
        statement = select(model)
        results = session.exec(statement).fetchall()

        if not results:
            console.print(f"[red]No [bold]{name}[/bold] found[/red]")
            return

        for item in results:
            console.print(item)


@app.command(rich_help_panel="Dev")
def all_cards() -> None:
    """List all cards."""
    engine = get_engine()
    list_all_from_table(engine, Card, "cards")


@app.command(rich_help_panel="Dev")
def all_categories() -> None:
    """List all categories."""
    engine = get_engine()
    list_all_from_table(engine, Category, "categories")


@app.command(rich_help_panel="Dev")
def all_practice_types() -> None:
    """List all practice types."""
    engine = get_engine()
    list_all_from_table(engine, PracticeType, "practice types")


@app.command(rich_help_panel="Dev")
def all_practice_sessions() -> None:
    """List all practice sessions."""
    engine = get_engine()
    list_all_from_table(engine, PracticeSession, "practice sessions")


@app.command(rich_help_panel="Dev")
def all_practice_history() -> None:
    """List all practice history."""
    engine = get_engine()
    list_all_from_table(engine, PracticeHistory, "practice history")


@app.command()
def delete():
    """Delete a card."""
    console.print("[red]Currently not implemented.")
    raise typer.Exit()


@app.command()
def practice():
    """Practice cards."""
    engine = get_engine()
    with Session(engine) as session:
        name = console.input("category: ")
        result = session.exec(select(Category).where(Category.name == name)).first()

        if result is None:
            console.print(f"[red]No category named {name}[/red]")
            return

        cards = result.cards

        method = Prompt.ask(
            "method: ", choices=available_practice_types.keys(), default="random"
        )

        practice_type = session.exec(
            select(PracticeType).where(PracticeType.name == method)
        ).first()

        if practice_type is None:
            practice_type = PracticeType(name=method)
            session.add(practice_type)
            session.commit()
            session.refresh(practice_type)

        practice_session = PracticeSession(practice_id=practice_type.id)
        session.add(practice_session)
        session.commit()
        session.refresh(practice_session)

        ordered_cards = available_practice_types[method](cards)

        n = IntPrompt.ask("max number of cards: ")
        max_tries = IntPrompt.ask("max number of tries: ")
        tries = 0
        for card in ordered_cards[:n]:
            while tries < max_tries:
                guess = console.input(f"what is the back of {card.front}? ")

                answered_correctly = exactly_correct(guess, card.back)
                practice_element = PracticeHistory(
                    card_id=card.id,
                    session_id=practice_session.id,
                    correct=answered_correctly,
                )
                session.add(practice_element)
                session.commit()
                if answered_correctly:
                    console.print("[green]Correct![/green]")
                    break
            else:
                console.print(
                    f"[red]Incorrect. The answer is[/red] [bold]{card.back}[/bold]"
                )

        practice_session.update_end_datetime()
        session.add(practice_session)
        session.commit()

    console.print(
        f"[green bold]Finished practicing {name} cards with {method} method[/green bold]"
    )
