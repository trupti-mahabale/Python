arr1 = [1, 2, 3, 4, 5]
arr2 = [None] * len(arr1)

for i in range(0, len(arr1)):
    arr2[i] = arr1[i]

print("Element of original array: ")
for i in range(0, len(arr1)):
    print(arr1[i])


print()


print("Element of new array: ")
for i in range(0, len(arr2)):
    print(arr2[i])