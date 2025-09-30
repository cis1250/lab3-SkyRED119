#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

myList = []

while (True):
  inpt = input()
  if (not inpt.isnumeric()):
    print("Please enter a positive integer.")
    continue
  if (int(inpt) <= 0):
    print("Please enter a positive integer.")
    continue
  inpt = int(inpt)
  break

def fib(lst: []):
    if len(lst) < 1:
        return 0
    elif len(lst) < 2:
        return 1
    else:
        return lst[-2] + lst[-1]

for i in range(inpt):
    myList.append(fib(myList))

print(myList)
