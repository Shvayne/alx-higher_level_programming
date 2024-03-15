#!/usr/bin/python3

import sys


def main():

    n = len(sys.argv)
    if n == 1:
        print("{} argument.".format(len(sys.argv)))

    elif n > 1:
        print("{} arguments:".format(len(sys.argv)))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
