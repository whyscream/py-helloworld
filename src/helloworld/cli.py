import sys

from .hello import hello


def main() -> None:
    """
    Allow executing the hello function from a CLI.

    An optional name of a person to greet is taken from the commandline, and the result is printed to stdout.
    """
    try:
        who = sys.argv[1]
        print(hello(who))
    except IndexError:
        print(hello())


if __name__ == "__main__":
    main()
