import math
weight=float(input("enter your wight in kg:"))
height=float(input("enter your height in m:"))
#baraye mesal 1.72m
bmi=(weight/(math.pow(height,2)))
if bmi<18.5:
    print("bmi:",bmi,"under weight")
elif bmi>=18.5 and bmi<24.9:
    print("bmi:",bmi,"normal weight")
elif bmi>=24.9 and bmi<29.9:
    print( "over weight")
elif bmi>=29.9 and bmi<34.9:
    print("bmi:",bmi,"obecity")
elif  bmi>=34.9 and bmi<39.9:
    print("bmi:",bmi," extreme obecity")
