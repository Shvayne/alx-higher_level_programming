#!/usr/bin/python3

import sys


def main():

    args_int = [int(arg) for arg in sys.argv[1:]]
    n = len(sys.argv)
    total = 0

    for i in range(1, n):
        total += int(sys.argv[i])
    print("{}".format(total))


if __name__ == "__main__":
    main()
