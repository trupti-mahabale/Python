# python program to multiply 2 lists
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]
print("Original list 1 : " +str(test_list1))
print("OriginaL list 2 : " +str(test_list2))
res_list = []
for i in range(0, len(test_list1)):
    res_list.append(test_list2[i] * test_list2[i])

print("Resultant list is : " + str(res_list))