edad=int(input("ingresa tu edad : "))
if edad<12:
    costo=50
    print(f"su pago de entrada sera de ${costo}")
elif  edad<18:
    costo=80
    print(f"su pago de entrada sera de ${costo}  ")
else:
    costo=120
    print(f"usted es mayor de edad su pago de entrada sera de ${costo}")