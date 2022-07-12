# from sre_constants import MAX_UNTIL


arr = [1, 2, 3, 4, 5]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
    if arr[i] < mini: mini = arr[i]


if arr[i] > maxi: maxi = arr[i]

print(mini)
print(maxi)