import argparse

from . import create_html, create_snippets, update_conid


def main():
    parser = argparse.ArgumentParser(description="Update [contest].id in config.toml")
    parser.add_argument("new_id", nargs="?", help="New ID value to set under [contest]")
    args = parser.parse_args()

    create_html.main()
    create_snippets.main()
    if args.new_id is not None:
        print(update_conid.main(args.new_id))
    return
