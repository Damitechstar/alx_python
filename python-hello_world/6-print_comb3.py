#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):  # Corrected line
        print("{:02d}, ".format(i) + "{:02d}".format(j), end="")
print()  # Print a new line at the end
