number=int(input("enter number"))
a=[]
for x in range(1,number+1):
    if number % x == 0:
     a.append(x)
print (a) 