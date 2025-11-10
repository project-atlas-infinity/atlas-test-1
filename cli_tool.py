# cli_tool.py - command line utility (Python 2)
import argparse
import os
from utils import list_py_files, read_file

def find_and_show(directory, name_substr):
    files = list_py_files(directory)
    matches = [f for f in files if name_substr in f]
    for fname in matches:
        print "----", fname, "----"
        print read_file(os.path.join(directory, fname))[:300]

def main():
    parser = argparse.ArgumentParser(description='Small CLI tool')
    parser.add_argument('--dir', default='.')
    parser.add_argument('--match', default='.py')
    args = parser.parse_args()
    find_and_show(args.dir, args.match)

if __name__ == '__main__':
    main()

# EOF
