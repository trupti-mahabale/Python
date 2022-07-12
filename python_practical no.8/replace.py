test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 9}
  

print("The original dictionary is : " + str(test_dict))
  

updict = {"Gfg"  : 10, "Best" : 17}
  
for sub in test_dict:
      
    
    if sub in updict:
        test_dict[sub]  = updict[sub]
  
print("The updated dictionary: " + str(test_dict)) 