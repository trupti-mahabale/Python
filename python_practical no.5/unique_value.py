# python program to count unique values inside a list
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
empty_list = []
count = 0
for ele in input_list:
    if(ele not in empty_list):
        count += 1
        empty_list.append(ele)

print("Count of unique values are : ", count)