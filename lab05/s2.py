#!/usr/bin/env python
import sys

#ile = open("/home/kschmidt/public_html/CS265/Labs/Python/students.csv", "r")
file = open(sys.argv[1], "r")

for line in file:
    l = line.strip('\n')
    w = l.split(',')
    name = w.pop(0)

    avg = 0
    for grade in w:
        avg += float(grade)

    avg /= len(w)
    print('{0}: {1}'.format(name, avg))
