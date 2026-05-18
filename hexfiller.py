import random
from tabulate import tabulate

def populate():
    features = ""
    ruin_rate = 0.3
    lair_rate = 0.3
    portal_rate = 0.1
    if random.random() < lair_rate:
        features = features + " lair"
    if random.random() < portal_rate:
        features = features + " portal"
    if random.random() < ruin_rate:
        features = features + " ruin"

    return features

def main():
    random.seed()
    rows, cols = 10, 10
    table_data = [[populate() for c in range(cols)] for r in range(rows)]

    print(tabulate(table_data, tablefmt="grid"))

if __name__ == "__main__":
    main()
