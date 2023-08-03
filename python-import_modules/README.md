Python - Import and Modules Project
This project consists of several tasks that involve importing modules, working with functions, handling exceptions, and understanding command-line arguments.

Task 0: Import a simple function from a simple file
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.

Instructions:
Use the print function with string formatting to display integers.
Assign the value 1 to a variable called a.
Assign the value 2 to a variable called b.
Use those two variables as arguments when calling the function add and print.
a and b must be defined in 2 different lines: a = 1 and another b = 2.
Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line.
You can only use the word add_0 once in your code.
You are not allowed to use * for importing or __import__.
Your code should not be executed when imported - by using __import__.
Task 1: How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.

Instructions:
The output should be:
Number of argument(s) followed by argument (if the number is one) or arguments (otherwise), followed by : (or . if no arguments were passed), followed by a new line.
If at least one argument is passed, print one line per argument: the position of the argument (starting at 1) followed by :, followed by the argument value and a new line.
Your code should not be executed when imported.
The number of elements of argv can be retrieved by using: len(argv).
You do not have to fully understand lists yet, but imagine that argv can be used just like a collection of arguments: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
Task 2: Everything can be imported.
Write a program that imports the variable a from the file variable_load_2.py and prints its value.

Instructions:
You are not allowed to use * for importing or __import__.
Your code should not be executed when imported.
Task 3: Integers division with debug
Write a function that divides 2 integers and prints the result.

Prototype: def safe_print_division(a, b):
You can assume that a and b are integers.
The result of the division should print on the finally section preceded by Inside result:.
Returns the value of the division, otherwise: None.
You have to use try: / except: / finally:.
You have to use "{ }".format() to print the result.
You are not allowed to import any module.
Task 4: Raise an exception
Write a function that raises a type exception.

Prototype: def raise_exception():
You are not allowed to import any module.
Task 5: Raise a message
Write a function that raises a name exception with a message.

Prototype: def raise_exception_msg(message=""):
You are not allowed to import any module.

This README file provides an overview of the project and its tasks.