"""
ETL-Query script
"""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "query",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "query":
        parser.add_argument("added_query")

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "query":
        query(args.added_query)

    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
