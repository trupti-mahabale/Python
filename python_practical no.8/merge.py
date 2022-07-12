# merge two list to form a disctionary
from collections import defaultdict
  
test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]
test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat', 'Nikhil', 'apple', 'grapes']
  

print("The original list1 is : " + str(test_list1))
print("The original list2 is : " + str(test_list2))
  
res = defaultdict(list)
for i, j in zip(test_list1, test_list2):
   res[i].append(j)

print("The merged key value dictionary is : " + str(dict(res)))