"""
Helpers Module
Contains custom utility functions for table calculations and greetings.
"""

import math


def tables_needed(people, seats):
    """Calculates the number of tables needed, rounding up to the nearest whole table."""
    return math.ceil(people / seats)


def welcome(name):
    """Returns a customized welcome message."""
    return f"Welcome to PLP, {name}!"


if __name__ == "__main__":
    # Test execution when run independently
    print(tables_needed(10, 4))