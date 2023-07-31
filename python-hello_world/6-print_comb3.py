#!/usr/bin/python3

 for i in range(1, 9):
    for j in range(i + 1, 10):
        end_str = ", " if i != 8 or j != 9 else "\n"
        print(f"{i}{j}", end=end_str)
       

