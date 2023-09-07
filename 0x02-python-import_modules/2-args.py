#!/usr/bin/python3
import sys

if len(sys.argv) == 2:
    print("1 argument")
    print("1: {}".format(sys.argv[1]))

elif len(sys.argv) > 2:
    count = 0
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in sys.argv[1:]:
        count += 1
        print("{}: {}".format(count, i))
else:
    print("0 arguments")
