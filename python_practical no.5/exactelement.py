# Exact element with frequency greater than k
from cgi import test


test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
print("The original list : " +str(test_list))
K = 2
res = []
for i in test_list:
    freq = test_list.count(i)

    if freq > K and i not in res:
        res.append(i)

print("The required element : " + str(res))