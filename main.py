def main(who: str) -> None:
    """a doctest in a docstring
    >>> main('World')
    Hello, World!
    """
    print(f"Hello, {who}!")


if __name__ == "__main__":
    main("World")
