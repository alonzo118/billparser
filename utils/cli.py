import argparse


def init_argparse() -> argparse.ArgumentParser:
    """Initialization of the ArgParser CLI tool with provided args."""
    parser = argparse.ArgumentParser(
        usage="%(prog)s [SEARCH] [OPTION]...",
        description="Finds matches to a given regular expression on Senate Resolutions Bills in the 116th session stored as XML files in a .zip archive",
    )
    parser.add_argument(
        "Search", metavar="search", type=str, help="the regular expression to match on"
    )
    parser.add_argument(
        "-t",
        "--text",
        action="store_true",
        help="enable the return of the matched summary text with highlighted matches",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} version 1.0.0"
    )
    return parser
