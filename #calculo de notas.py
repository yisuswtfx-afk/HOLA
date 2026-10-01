#calculo de notas 
print ("calculo de notas")
nota1 = float(input("ingrese la primera nota parcial: "))
nota2 = float(input("ingrese la segunda nota parcial: "))
nota3 = float(input("ingrese la tercera nota parcial: "))

promedio1 = nota1 + nota2 + nota3 / 3
nota_inicial = promedio1 * 0.4
print(nota_inicial)
examen = float(input("ingrese la nota de su examen: "))
nota_examen = examen * 0.5
print(nota_examen)


trabajo_final = float(input("ingrese su nota del trabajo final: "))
nota_trabajo = trabajo_final * 0.1
print(nota_trabajo)
nota_total = nota_trabajo + nota_inicial + nota_examen
print("su nota final es:", nota_total)

if nota_total < 3:
    print("el estudiante reprobo")

else:
    print("el estudiante aprobo")
    
