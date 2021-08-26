import click
from pathlib import Path

from .file_update_handler import FileUpdateHandler
from .db import init_db


@click.command()
def main():
    """
    wizdiff
    """
    if not Path("wizdiff.db").exists():
        # add initial data to compare here
        print("initing db")
        init_db()

    update_handler = FileUpdateHandler()
    update_handler.update_loop()


if __name__ == "__main__":
    main()
