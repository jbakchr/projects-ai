# src/cli.py

import argparse
from rag import query_projects


def main():
    parser = argparse.ArgumentParser(
        description="Ask questions about your projects using AI"
    )

    parser.add_argument(
        "command",
        choices=["ask"],
        help="Command to run (only 'ask' supported for now)",
    )

    parser.add_argument(
        "query",
        help="Your question about your projects",
    )

    args = parser.parse_args()

    if args.command == "ask":
        print("\n🔍 Question:")
        print(args.query)

        print("\n🤖 Answer:")
        response = query_projects(args.query)
        print(response)
        print()


if __name__ == "__main__":
    main()
