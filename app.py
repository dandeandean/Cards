import typer
from rich import print
from rich.console import Console
from rich.table import Table
from Cards import Card, Database
import random
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
    
@app.command()
def show_cards():
    cards = db.cards_from_db()
    table = Table("Front", "Back","Box")
    for card in cards:
        table.add_row(card.get_front(),card.get_back(),str(card.get_current_bin()))
    con.print(table)

@app.command()
def delete(front: str, back: str):
    # This needs to be implemented in Database
    db.delete_card(front,back)

@app.command()
def practice(n:int=10):
    boxes = [db.cards_by_box(0), db.cards_by_box(1),db.cards_by_box(2),db.cards_by_box(3),db.cards_by_box(4)] 
    box_lens = [len(box) for box in boxes]
    #r = random.sample(boxes[0],9)
    print(boxes,box_lens)

# The main thing
if __name__ == "__main__":
    app()
