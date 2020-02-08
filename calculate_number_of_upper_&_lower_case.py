s = input("Enter Number: ")
d={"Upper":0, "Lower":0}
for c in s:
    if c.isupper():
        d["Upper"]+=1
    elif c.islower():
        d["Lower"]+=1
    else:
        pass
print ("Upper", d["Upper"])
print ("Lower", d["Lower"])