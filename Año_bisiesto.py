año=int(input("ingresa un año : "))
if año % 400==0:
    print("es un año bisiesto ")
elif año % 100==0:
    print("no es un año bisiento")
elif año % 4==0:
    print("es un año bisiesto")
else:
    print("no es un año bisiesto")