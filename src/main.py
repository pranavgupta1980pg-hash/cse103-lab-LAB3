"""CSE103 Lab 3 - entry point.

Simple demo used to verify the repository structure and test setup.
"""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the demo."""
    print(greet("CSE103"))


if __name__ == "__main__":
    main()
