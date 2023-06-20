import typer
from rich import print
from rich.console import Console
from rich.table import Table
from Cards import Card, Database
con = Console()
app = typer.Typer()
db = Database()

@app.command()
def sayhello(name: str):
    print(f"hello {name}!")

@app.command()
def saygoodbye(name: str):
    print(f"goodbye {name}!")

@app.command()
def new(front: str, back: str):
    #TODO add optional
    new_card = Card(front,back)
    db.push_card(new_card)
    print(f"added card {new_card}")

def main():
    cards = db.cards_from_db()
    table = Table("Front", "Back","Box")
    for card in cards:
        table.add_row(card.get_front(),card.get_back(),str(card.get_current_bin()))
    con.print(table)

if __name__ == "__main__":
    app()
