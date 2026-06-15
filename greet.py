"""Greeter utility — prints a friendly hello message."""

import argparse
from datetime import datetime


def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    now = datetime.now().strftime("%H:%M")
    return f"[{now}] Hello, {name}!"


def main():
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
