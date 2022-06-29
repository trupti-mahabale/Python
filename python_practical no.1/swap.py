#PROGRAM TO SWAP TWO VARIABLES
a = float(input("Please enter the first value a: "))
b = float(input("Please enter the second value b: "))
print("Before swapping two number: a ={0} and b = {1}".format(a, b))
a=a+b
b=a-b
a=a-b
print("After swapping two number: a ={0} and b = {1}".format(a, b))
