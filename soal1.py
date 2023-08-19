import math
print("welcome to my calculator")
print("+:sum")
print("-:sub")
print("*:mul")
print("/:div")
print("cos")
print("sin")
print("tan")
print("log")
print("sqrt")
print("factorial")

print("enter your choise:")
op=input(" operator:")
if op=="+" or op=="-" or op=="*" or op=="/":      
    a=float(input("get num1:"))
    b=float(input("get num2:"))
else:
        a=float(input("get num1:"))
if op=="+":
    result=a+b
elif op=="-":
    result=a-b
elif op=="*":
    result=a*b
elif op=="/":
    if b==0:
        result="can not devide by zero"
    else:
        result=a/b

elif op=="sqrt":
    result=math.sqrt(a)
elif op=="sin":
    result=math.sin(math.radians(a))
elif op=="cos":
    result=math.cos(math.radians(a))
elif op=="tan":
    result=math.tan(math.radians(a))
elif op=="cot":
    result=1/(math.tan(math.radians(a)))

elif op=="log":
    result=math.log(a)
elif op=="factorial":
    result=math.factorial(int(a))


print(result)
