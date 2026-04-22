import argparse
import sys

from bbb_render import download
from bbb_render import make_xges

def main(argv=None):
    parser = argparse.ArgumentParser(prog="bbb-render")
    subparsers = parser.add_subparsers(dest="command", required=True)

    download_parser = subparsers.add_parser(
        "download",
        help="Download a BigBlueButton presentation",
    )
    download_parser.add_argument('arg', nargs='*')
    download_parser.set_defaults(func=download.main)

    make_xges_parser = subparsers.add_parser(
        "make-xges",
        help="Generate a GES project from downloaded assets",
    )
    make_xges_parser.add_argument('arg', nargs='*')
    make_xges_parser.set_defaults(func=make_xges.main)

    args = parser.parse_args(argv)

    if argv is None:
        argv = sys.argv

    argv.pop(0)

    return args.func(argv)

if __name__ == "__main__":
    raise SystemExit(main())