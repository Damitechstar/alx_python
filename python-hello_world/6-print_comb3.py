#!/usr/bin/python3

for i in range(1, 10):
    for j in range(i + 1, 10):
        print(f"{i:0d}{j:0d}", end=", " if i != 8 or j != 9 else "\n")