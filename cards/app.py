from typing import List, Optional

import typer

from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.panel import Panel
from sqlmodel import Session, select
import os

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

def print_card(card: Card, category: Category = None):
    if category == None:
        category = card.categories[0].name
    console.print(Panel.fit(f"{card.front} | {card.back}",title=f"{category}"))


@app.command()
def new():
    """Create a new card."""
    console.print("Creating a new card...")
    name = console.input("category: ")

    engine = get_engine()
    with Session(engine) as session:
        category = session.exec(select(Category).where(Category.name == name)).first()

        if category is None:
            # Create
            category = Category(name=name)

        front = console.input("front: ")
        back = console.input("back: ")
        card = Card(front=front, back=back, categories=[category])
        session.add(card)
        session.commit()

        session.refresh(card)

    console.print(f"[green]Created card: {card}[/green]")


def cards_for_category(name: str, session) -> List[Card]:
    category = session.exec(select(Category).where(Category.name == name)).first()

    if category is None:
        console.print(f"[red]No category named {name}[/red]")
        raise typer.Exit(code=1)

    return category.cards

def category_id_to_name(id: int, session) -> str:
    category = session.exec(select(Category).where(Category.id == id)).first()
    if category is None:
        console.print(f"[red]Invalid category ID {id}[/red]")
        raise typer.Exit(code=1)

    return category.name


@app.command()
def ls():
    """List cards in a category."""
    console.print("Categories")
    all_categories()
    desired_category = console.input("category: ")

    engine = get_engine()
    with Session(engine) as session:
        # check if they passed the ID
        if desired_category.isnumeric():
            desired_category = category_id_to_name(desired_category,session)


        cards = cards_for_category(desired_category, session)

        table = Table("Front", "Back")
        for card in cards:
            # console.print(card)
            table.add_row(card.front, str(card.back))

        console.print(table)


def get_all_from_table(session, model, name: str) -> List:
    statement = select(model)
    results = session.exec(statement).fetchall()

    if not results:
        console.print(f"[red]No [bold]{name}[/bold] found[/red]")
        raise typer.Exit(code=1)

    return results


def list_all_from_table(session, model, name: str, max_to_show: Optional[int] = None):
    results = get_all_from_table(session, model, name)

    total = len(results)
    n_to_show = max_to_show or total

    for item in results[:n_to_show]:
        print_card(item)
        print(type(item) == Card)
        console.print(item)

    if total > n_to_show:
        console.print(f"... and {total - n_to_show} more")


@app.command(rich_help_panel="Dev")
def all_cards(show_all: bool = False) -> None:
    """List all cards."""
    max_to_show = None if show_all else 10
    engine = get_engine()
    with Session(engine) as session:
        list_all_from_table(session, Card, "cards", max_to_show=max_to_show)
    

@app.command(rich_help_panel="Dev")
def all_categories() -> None:
    """List all categories."""
    engine = get_engine()
    with Session(engine) as session:
        # list_all_from_table(session, Category, "categories")
        cats = get_all_from_table(session, Category, "categories")

    table = Table("Category", "ID")
    for cat in cats:
        table.add_row(cat.name, str(cat.id))
    console.print(table)



@app.command(rich_help_panel="Dev")
def all_practice_types() -> None:
    """List all practice types."""
    engine = get_engine()
    with Session(engine) as session:
        list_all_from_table(session, PracticeType, "practice types")


@app.command(rich_help_panel="Dev")
def all_practice_sessions() -> None:
    """List all practice sessions."""
    engine = get_engine()
    with Session(engine) as session:
        list_all_from_table(session, PracticeSession, "practice sessions")


@app.command(rich_help_panel="Dev")
def all_practice_history() -> None:
    """List all practice history."""
    engine = get_engine()
    with Session(engine) as session:
        list_all_from_table(session, PracticeHistory, "practice history")

@app.command()
def delete_all(rich_help_panel="Dev") -> None:
    """Delete the database of cards."""
    console.print("[red]Currently not implemented.")
    raise typer.Exit()

@app.command()
def delete(front: str, back: str) -> None:
    """Delete a card."""
    # console.print("[red]Currently not implemented.")
    engine = get_engine()
    with Session(engine) as session:
        statement = select(Card).where(Card.front == front and Card.back == back)
        results = session.exec(statement)
        card = results.first()
        if card is None:
            console.print(f"[red]No such card: {front} | {back}[/red]")        
            return
        session.delete(card)
        session.commit()
    console.print(f"[red]Deleted card: {card}[/red]")        



@app.command()
def practice(
    forward: bool = typer.Option(
        True, "--forward/--backward", help="Practice cards forward or backward."
    )
) -> None:
    """Practice cards."""
    engine = get_engine()
    with Session(engine) as session:
        categories = get_all_from_table(session, Category, "categories")
        category_names = [category.name for category in categories]
        name = Prompt.ask("category: ", choices=category_names)

        cards = cards_for_category(name, session)

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

        n = IntPrompt.ask("max number of cards: ", default=min(3, len(cards)))
        max_tries = IntPrompt.ask("max number of tries: ", default=3)
        tries = 0
        for card in ordered_cards[:n]:
            # TODO: Isolate this to allow for different practice types
            while tries < max_tries:
                side, question, correct_answer = (
                    ("front", card.front, card.back)
                    if forward
                    else ("back", card.back, card.front)
                )

                guess = console.input(f"what is the {side} of {question!r}? ")
                # TODO: Look up in database if alternatives are correct
                answered_correctly = exactly_correct(guess, correct_answer)

                practice_element = PracticeHistory(
                    card_id=card.id,
                    session_id=practice_session.id,
                    guess=guess,
                    correct=answered_correctly,
                )
                session.add(practice_element)
                session.commit()
                if answered_correctly:
                    console.print("[green]Correct![/green]")
                    break

                tries += 1
                console.print(
                    f"[red]Incorrect. Try again. ({tries} / {max_tries})[/red]"
                )
            else:
                tries = 0
                console.print(
                    f"[red]Incorrect. The answer is[/red] [bold]{card.back}[/bold]"
                )

        practice_session.update_end_datetime()
        session.add(practice_session)
        session.commit()

    console.print(
        f"[green bold]Finished practicing {name} cards with {method} method[/green bold]"
    )
