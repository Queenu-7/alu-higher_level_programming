#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # exclude the script name itself
    count = len(args)

    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, "" if count == 1 else "s"))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
