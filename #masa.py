#masa
presion = float(input("ingrese la presion: "))
volumen = float(input("ingrese el volumen: "))
temperatura = float(input("ingrese la temperatura: "))
masa = presion * volumen / 0.37 * (temperatura + 460)
print ("la masa es: ", masa)