# Create a Lambda Function that takes one argument and triples the argument passed in it.
# The input should be from the User.

triple = lambda x: x * 3

print(triple(int(input("Enter a number to triple it: "))))