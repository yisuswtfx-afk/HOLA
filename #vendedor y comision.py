#vendedor y comision
print ("calculo de comision")
sueldo_base = float(input("Ingrese el sueldo base: "))
numero_ventas = int(input("Ingrese el numero de ventas realizadas: "))
ventas = float(input("Ingrese el monto total de ventas realizadas: "))

if numero_ventas >= 1:
    print ("se usa un bono")
    bono = sueldo_base * (0.10 * numero_ventas)
    print ("su sueldo es", bono)

else:
    print("su sueldo es", sueldo_base)



