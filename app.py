import typer
from rich import print
app = typer.Typer()

@app.command()
def sayhello(name: str):
    print(f"hello {name}!")


if __name__ == "__main__":
     app()

