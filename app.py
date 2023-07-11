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
def ls():
    cards = db.cards_from_db()
    table = Table("Front", "Back","Box")
    for card in cards:
        table.add_row(card.get_front(),card.get_back(),str(card.get_current_bin()))
    con.print(table)

@app.command()
def delete(front: str, back: str):
    # This needs to be implemented in Database
    db.delete_card(front,back)
    
def get_prac_choices(n: int=10):
    boxes = [db.cards_by_box(0), db.cards_by_box(1),db.cards_by_box(2),db.cards_by_box(3)] 
    box_lens = [len(box) for box in boxes]
    # correct for if there's not enough cards in the field
    if n > sum(box_lens):
        n = sum(box_lens)
    # get correct lens of choices
    choice_lens = [0]*len(box_lens)
    choices = list()
    # get ideal len for each box we want
    for i in range(len(box_lens)): 
        choice_lens[i] = n//2**(i+1)
        if choice_lens[i] == 0: 
            choice_lens[i] += 1
            break
        # correct for idealism
        if choice_lens[i] > box_lens[i]:
            choice_lens[i] = box_lens[i]

    # pad
    i = 0
    # TODO find better way of doing this
    while(sum(choice_lens) < n):
       if choice_lens[i] < box_lens[i]: choice_lens[i] += 1
       i += 1
       i = i % len(choice_lens)

    # get the choices
    for i in range(len(box_lens)):
        r = random.sample(boxes[i],choice_lens[i])
        choices.append(r)

    return choices


@app.command()
def practice(n: int= typer.Argument(default=10)):
    choices = get_prac_choices(n)
    for deck in choices:
        for card in deck:
            res = card.practice()
            if (res):
                new_bin = card.get_current_bin() + 1
                if new_bin > 3: new_bin = 3
                db.set_box(card.get_front(),card.get_back(),new_bin)



    

# The main thing
if __name__ == "__main__":
    app()
