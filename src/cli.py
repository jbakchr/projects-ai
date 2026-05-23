# src/cli.py

import argparse
import threading
import time

from rag import query_projects

def spinner(stop_event):
    symbols = ["|", "/", "-", "\\"]
    i = 0

    while not stop_event.is_set():
        print(f"\r⏳ Thinking... {symbols[i % len(symbols)]}", end="")
        time.sleep(0.1)
        i += 1

    print("\r", end="")  # Clear line


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
        print("\n🔍 Question:\n")
        print(args.query)

        print("\n🤖 Answer:\n")

        stop_event = threading.Event()
        spinner_thread = threading.Thread(target=spinner, args=(stop_event,))
        spinner_thread.start()

        # Run query
        response = query_projects(args.query)

        # Stop spinner
        stop_event.set()
        spinner_thread.join()

        print(response)
        print("\n")



if __name__ == "__main__":
    main()
