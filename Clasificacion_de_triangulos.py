lado1=float(input("Ingresa la longitud del lado 1  : "))
lado2=float(input("ingresa la longitud del lado 2  : "))
lado3=float(input("ingresa la longitud del lado 3  : "))

if lado1==lado2 and lado2==lado3:
    print("Es un triangulo equilatero")
elif lado1==lado2:
    print("Es un triangulo isosceles")
elif lado1==lado3:
    print("Es un triangulo isosceles")
elif lado2==lado3:
    print("Es un triangulo isosceles")
else:
    print("es un triangulo escaleno")

    