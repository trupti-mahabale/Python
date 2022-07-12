# python program to print intersection of 2 lists
def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
list1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
list2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(list1, list2))