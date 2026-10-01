#tienda con descuento
print("factura")
pago = float(input("el total de su compra es: "))
descuento = 0.15
descuento_total = pago * 0.15
pago_final = pago - descuento_total 
print ("su descuento es de: ", descuento_total)
print ("el precio final es de:", pago_final)
