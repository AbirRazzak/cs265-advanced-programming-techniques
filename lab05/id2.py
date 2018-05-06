#!/usr/bin/env python
import sys

argc = len(sys.argv)
if argc > 1:
    file = open(sys.argv[1], "r")
else:
    file = sys.stdin

#file = open("/home/kschmidt/public_html/CS265/Labs/Python/ids", "r")
dict = {}

for line in file:
    data = line.strip('\n').split(' ', 1)
    id = data[0]
    value = data[1]
    dict[id] = value

for key in dict:
    print('{0} {1}'.format(key, dict[key]))
