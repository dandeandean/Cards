## Dependencies 
    
    pip install "typer[all]"


## Start Up

```bash 
poetry install 
poetry shell 

# Once in the environment
python scripts/populate-db.py
```

## Usage

```bash 
practice --help
```

```text

 Usage: practice [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.         │
│ --show-completion             Show completion for the current shell, to copy it │
│                               or customize the installation.                    │
│ --help                        Show this message and exit.                       │
╰─────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────╮
│ delete                Delete a card.                                            │
│ ls                    List cards in a category.                                 │
│ new-card              Create a new card.                                        │
│ practice              Practice cards.                                           │
╰─────────────────────────────────────────────────────────────────────────────────╯
╭─ Dev ───────────────────────────────────────────────────────────────────────────╮
│ all-cards                           List all cards.                             │
│ all-categories                      List all categories.                        │
│ all-practice-history                List all practice history.                  │
│ all-practice-sessions               List all practice sessions.                 │
│ all-practice-types                  List all practice types.                    │
╰─────────────────────────────────────────────────────────────────────────────────╯

```