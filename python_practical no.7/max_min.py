# maximum and minimum elements in tuple
test_tup = (5, 20, 3, 7, 6, 8)
print("The original tuple is : " + str(test_tup))
K = 2
res = []
test_tup = list(sorted(test_tup))

for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)
print("The extracted values : " + str(res))
