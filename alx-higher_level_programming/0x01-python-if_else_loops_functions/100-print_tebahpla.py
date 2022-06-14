#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((c - (ord('a') - ord('A'))) if c % 2 else c), end='')
