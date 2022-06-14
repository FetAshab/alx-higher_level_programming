#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    number = len(sys.argv)
    for solution in range(1, number):
        add += int(sys.argv[solution])
    print(add)
