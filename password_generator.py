"""
Password Generator Module
Creates random passwords of custom or default lengths using ASCII letters and digits.
"""

import random
import string


def make_password(length=8):
    """Generates a random password of a specified length."""
    characters = string.ascii_letters + string.digits
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


if __name__ == "__main__":
    # Generate passwords with default (8) and custom (12) lengths
    p1 = make_password()
    p2 = make_password(12)

    print("Password:", p1)
    print("Length:", len(p1))
    print("Password:", p2)
    print("Length:", len(p2))