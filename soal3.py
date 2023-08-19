a=input("enter your name:")
b=input("enter your family:")
c=float(input("nomre1:"))
d=float(input("nomre2:"))
e=float(input("nomre3:"))
mean=(c+d+e)/3
if mean>=17:
    print("your condition is great ")
elif mean<17 and mean>=12:
    print("your condition is normal")
elif mean<12 and mean>=0:
    print("your are failed ")
else:
    print("your calculation is wrong")
