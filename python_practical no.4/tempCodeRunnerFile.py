a = eval(input("Enter diamond's height: "))
for x in range(a):
    print(" " * (a - x), "*" * (2*x + 1))
for x in range(a - 2, -1, -1):
    print("  " * (a - x), "*" * (2*x + 1)) 