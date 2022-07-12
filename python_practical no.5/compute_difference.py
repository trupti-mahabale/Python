# python program to  compute difference between two list
def Diff(A, B):
    print("Differenc of two lists :: >")
    return (list(set(A) - set(B)))

A = list()
n1 = int(input("Enter the size of the first List ::"))
print("Enter the element of first List ::")
for i in range(int(n1)):
    k = int(input(" "))
    A.append(k)
B = list()
n2 = int(input("Enter the size of the second List :: "))
print("Enter the Element of second List ::")
for i in range(int(n2)):
    k = int(input(" "))
    B.append(k)
print(Diff(A, B))