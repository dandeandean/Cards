## Dependencies 
    
    pip install "typer[all]"


## Start Up

```bash 
poetry install 
poetry shell 

# Once for example data
python scripts/populate-db.py
```

## Usage

```bash 
card --help
```

```text
 Usage: card [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                   │
│ --show-completion             Show completion for the current shell, to copy it or        │
│                               customize the installation.                                 │
│ --help                        Show this message and exit.                                 │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────╮
│ delete                  Delete a card.                                                    │
│ ls                      List cards in a category.                                         │
│ new                     Create a new card.                                                │
│ practice                Practice cards.                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Dev ─────────────────────────────────────────────────────────────────────────────────────╮
│ all-cards                                List all cards.                                  │
│ all-categories                           List all categories.                             │
│ all-practice-history                     List all practice history.                       │
│ all-practice-sessions                    List all practice sessions.                      │
│ all-practice-types                       List all practice types.                         │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
```

Practice the cards for a category

```bash
card practice
category:  [German/German Verbs/Basic German/French/Statistics/Country Capitals/Capitals]: German
method:  [random/same/most-recent] (random):
max number of cards:  (3):
max number of tries:  (3):
what is the back of "you're welcome"? bitte
Incorrect. Try again. (1 / 3)
what is the back of "you're welcome"? Bitte
Incorrect. Try again. (2 / 3)
what is the back of "you're welcome"? Gern geschehen
Incorrect. Try again. (3 / 3)
Incorrect. The answer is bitte schön
what is the back of "I'm a teacher"? Ich bin Lehrer
Correct!
what is the back of 'goodbye'? Auf Wiedersehen
Correct!
Finished practicing German cards with random method
```

Practicing will log all the practice history into a local data base.

Practice history data 

```bash
card all-practice-history
PracticeHistory(session_id=1, guess='bitte', datetime='2023-07-30T10:56:34.608060', id=1, card_id=20, correct=False)
PracticeHistory(session_id=1, guess='Bitte', datetime='2023-07-30T10:56:36.309292', id=2, card_id=20, correct=False)
PracticeHistory(session_id=1, guess='Gern geschehen', datetime='2023-07-30T10:56:43.248711', id=3, card_id=20, correct=False)
PracticeHistory(session_id=1, guess='Ich bin Lehrer', datetime='2023-07-30T10:56:53.549436', id=4, card_id=15, correct=True)
PracticeHistory(session_id=1, guess='Auf Wiedersehen', datetime='2023-07-30T10:57:06.146497', id=5, card_id=2, correct=True)
```