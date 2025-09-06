num1=int(input("ingresa el primer numero  : "))
num2=int(input("ingresa un segundo numero:"))
num3=int(input("ingresa un tercer numero : "))
if num1>=num2 and num1>=num3:
    nummayor=num1
elif num2>=num1 and num2>=num3:
    nummayor=num2
else:
    nummayor=num3
if num1<=num2 and num1<=num3:
    nummenor=num1
elif num2<=num1 and num2<=num3:
    nummenor=num2
else:
    nummenor=num3

print(f"El numero mayor es:{nummayor} ")
print(f"el numero menor es : {nummenor}")