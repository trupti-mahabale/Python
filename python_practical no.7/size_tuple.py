# find size of tuple
import sys
tup1 = ("Studytonight", 1,2,3)
tup2 = ("Python","java","C++")
tup3 = ((1,2),(4,6),(7,2),(10,9))

print("Size of tup1: ",sys.getsizeof(tup1), "bytes")
print("Size of tup2: ",sys.getsizeof(tup2), "bytes")
print("Size of tup3: ",sys.getsizeof(tup3), "bytes")