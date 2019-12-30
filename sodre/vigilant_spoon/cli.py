"""Console script for vigilant-spoon."""

import sys
import click


@click.command()
def vigilant_spoon(args=None):
    """Console script for vigilant-spoon."""
    # fmt: off
    click.echo("Replace this message by putting your code into "
               "vigilant_spoon.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    # fmt: on
    return 0


if __name__ == "__main__":
    sys.exit(vigilant_spoon)  # pragma: no cover
