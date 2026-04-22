import argparse

from bbb_render import download
from bbb_render import make_xges

def main(argv=None):
    parser = argparse.ArgumentParser(prog="bbb-render")
    subparsers = parser.add_subparsers(dest="command", required=True)

    download.register_subcommand(subparsers)
    make_xges.register_subcommand(subparsers)

    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())