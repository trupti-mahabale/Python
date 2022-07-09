def isPronicNumber(num):
    flag = False

    for j in range(1, num+1):
        if((j*(j+1)) == num):
            flag = True

            break

    return flag

print("Pronic Number between 1 to 100: ")

for i in range(1, 101):
    if(isPronicNumber(i)):
        print(i)
        print("")