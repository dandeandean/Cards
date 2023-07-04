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
def new(front: str, back: str, bin: int=0):
    #TODO add optional
    new_card = Card(front,back,bin)
    db.push_card(new_card)
    print(f"added card {new_card}")
    
@app.command()
def show():
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
    boxes = [db.cards_by_box(0), db.cards_by_box(1),db.cards_by_box(2),db.cards_by_box(3)] 
    box_lens = [len(box) for box in boxes]
    if n > sum(box_lens):
        n = sum(box_lens)
        print(n)
    choice_lens = [0]*len(box_lens)
    choices = list()
    for i in range(len(box_lens)):
        choice_lens[i] = box_lens[i]//(i+1)
    #r = random.sample(boxes[0],n)
    print(boxes,box_lens)
    print(choice_lens)

# The main thing
if __name__ == "__main__":
    app()
