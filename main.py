"""Example project for poetry, lint, test, (pre-commit) and automatic doc generation
Functions:
  `main(who)` - Ptint "Hello, {who}!"
"""


def main(who: str) -> None:
    """Print Hello to whatewer You want.

    Examples:
        >>> main('World')
        Hello, World!

    Args:
        who: Who to greet.

    """
    print(f"Hello, {who}!")


if __name__ == "__main__":
    main("World")
