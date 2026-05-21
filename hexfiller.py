import random
import click
from tabulate import tabulate


def populate(lair_rate, portal_rate, ruin_rate):
    features = ""
    if random.random() < lair_rate:
        features += " lair"
    if random.random() < portal_rate:
        features += " portal"
    if random.random() < ruin_rate:
        features += " ruin"
    return features


@click.command()
@click.option("--rows", default=10, show_default=True, help="Number of rows in the grid.")
@click.option("--cols", default=10, show_default=True, help="Number of columns in the grid.")
@click.option("--lair-rate", default=0.3, show_default=True, type=click.FloatRange(0.0, 1.0), help="Spawn probability for lairs.")
@click.option("--portal-rate", default=0.1, show_default=True, type=click.FloatRange(0.0, 1.0), help="Spawn probability for portals.")
@click.option("--ruin-rate", default=0.3, show_default=True, type=click.FloatRange(0.0, 1.0), help="Spawn probability for ruins.")
@click.option("--seed", default=None, type=int, help="Random seed for reproducible output.")
def main(rows, cols, lair_rate, portal_rate, ruin_rate, seed):
    """Generate a randomised feature map and print it as a grid."""
    random.seed(seed)
    table_data = [
        [populate(lair_rate, portal_rate, ruin_rate) for _ in range(cols)]
        for _ in range(rows)
    ]
    print(tabulate(table_data, tablefmt="grid"))


if __name__ == "__main__":
    main()
