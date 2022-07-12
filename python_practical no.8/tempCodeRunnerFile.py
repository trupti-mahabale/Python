test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2, "for" : 3, "Geeks" : 2}
  

print("The original dictionary is : " + str(test_dict))
  

res = {val[0] : val[1] for val in sorted(test_dict.items(), key = lambda x: (-x[1], x[0]))}
  

print("Sorted dictionary : " + str(res)