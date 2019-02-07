import argparse
import sys


def diff(destination, source):
    set_des = set(destination)
    set_source = set(source)

    return list(set_source - set_des)


def arg_parser():
    argp = argparse.ArgumentParser()
    argp.add_argument('-d', dest='destination', required=True)
    argp.add_argument('-s', dest='source', required=True)

    options = argp.parse_args(sys.argv[1:])
    return options.destination, options.source
