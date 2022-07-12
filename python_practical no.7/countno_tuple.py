# python program to count number of tuple in a list
from dataclasses import dataclass


data = (2,4,6,8,10)
print(data)
count=data.count
print("Occurences: ",count)
data = (2,4,6,8,10,2)
print(data)
count = data.count(2)
print("Occurences: ",count)