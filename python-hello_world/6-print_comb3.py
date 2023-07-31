#!/usr/bin/python3
output = ""
for i in range(10):
    for j in range(i + 1, 10):
        output += "{:d}{:d}, ".format(i, j)
print(output[:-2])