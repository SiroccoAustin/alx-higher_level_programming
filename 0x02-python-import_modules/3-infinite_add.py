#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0

    if len(sys.argv) < 2:
        print(total)
    else:
        for i in sys.argv[1:]:
            total += int(i)
        print(total)
