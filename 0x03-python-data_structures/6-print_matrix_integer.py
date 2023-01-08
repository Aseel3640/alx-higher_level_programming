#!/usr/bin/python3
for i in matrix:
    for j in i:
        print("{:d}".format(j), end="" if j == i[-1] else " ")
    print()
