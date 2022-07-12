# program to concatenate two list
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

for i in test_list2:
    test_list1.append(i)

print("Concatenated list using naive method : "+str(test_list1))