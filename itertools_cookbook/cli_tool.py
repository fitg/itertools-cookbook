import click
import itertools

@click.group()
def cli():
    pass

@cli.command()
@click.argument('items', nargs=-1)
@click.option('--r', default=2, help='Length of combinations (e.g. --r 2)')
def combo(items, r):
    """
    Show combinations of ITEMS taken R at a time. (i.e. combo A B C --r 2)

    Example:
        python cli_tool.py combo A B C --r 2
        Output:
        ('A', 'B')
        ('A', 'C')
        ('B', 'C')
    """
    for c in itertools.combinations(items, r):
        print(c)

@cli.command()
@click.argument('items', nargs=-1)
@click.option('--r', default=2, help='Length of permutations (e.g. --r 2)')
def perm(items, r):
    """
    Show permutations of ITEMS taken R at a time. (i.e. perm A B C --r 2)

    Example:
        python cli_tool.py perm A B C --r 2
        Output:
        ('A', 'B')
        ('A', 'C')
        ('B', 'A')
        ('B', 'C')
        ('C', 'A')
        ('C', 'B')
    """
    for p in itertools.permutations(items, r):
        print(p)

@cli.command()
@click.argument('list1', nargs=-1)
@click.option('--list2', multiple=True, help='Second list of elements (e.g. --list2 X Y)')
def cartesian(list1, list2):
    """
    Show Cartesian product of two lists. (i.e. cartesian 1 2 --list2 A B)

    Example:
        python cli_tool.py cartesian 1 2 --list2 A B
        Output:
        ('1', 'A')
        ('1', 'B')
        ('2', 'A')
        ('2', 'B')
    """
    for pair in itertools.product(list1, list2):
        print(pair)

@cli.command()
def slice_infinite():
    """Demo: First 5 odd numbers starting from 1.
    
    """
    odd_numbers = itertools.islice(itertools.count(1, 2), 5)
    slice = list(odd_numbers)
    print(slice)

@cli.command()
def round_robin_teams():
    """Demo: Cycle through teams in a round-robin.
    
    """
    teams = ['Red', 'Blue', 'Green']
    cycler = itertools.cycle(teams)
    round_robin_teams = [next(cycler) for _ in range(10)]
    print(round_robin_teams)

@cli.command()
def flatten_nested():
    """Demo: Flatten a list of lists using chain.
    
    """
    nested = [[1, 2], [3, 4], [5]]
    flatten_nested = list(itertools.chain.from_iterable(nested))
    print(flatten_nested)

@cli.command()
def pairwise_sum():
    """Demo: Create all unique pairs and sum them.
    
    """
    numbers = [1, 2, 3]
    pairs = itertools.combinations(numbers, 2)
    pairwise_sum = [(a, b, a + b) for a, b in pairs]
    print(pairwise_sum)

@cli.command()
def filter_even_combinations():
    """Demo: 3 numbers which sum to even.
    
    """
    numbers = [1, 2, 3, 4]
    combos = itertools.combinations(numbers, 3)
    filter_even_combinations = [c for c in combos if sum(c) % 2 == 0]
    print(filter_even_combinations)

if __name__ == '__main__':
    cli()