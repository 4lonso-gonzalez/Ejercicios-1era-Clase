#Ejercicio 2
ingreso = int(input("Ingrese el ingreso del comprador: "))
casa = int(input("Ingrese el costo de la casa: "))

#Opción 1
"""
if ingreso >= 80000:
    pie = (casa * 0.15)
    mensual = (casa - pie)/120
    print("Por el concepto de pie el comprador debe pagar: ",pie,"CLP")
    print("Cada mensualidad a pagar por 10 años saldrian cada una a: ",mensual,"CLP")
elif ingreso < 80000:
    pie = (casa * 0.30)
    mensual = (casa - pie)/84
    print("Por el concepto de pie el comprador debe pagar: ",pie,"CLP")
    print("Cada mensualidad a pagar por 10 años saldrian cada una a: ",mensual,"CLP")
else:
    print("El ingreso del comprador no es valido para la empresa")
"""
#Opción 2
"""
condicional = 0
while condicional == 0:
    if ingreso >= 80000:
    pie = (casa * 0.15)
    mensual = (casa - pie)/120
    print("Por el concepto de pie el comprador debe pagar: ",pie,"CLP")
    print("Cada mensualidad a pagar por 10 años saldrian cada una a: ",mensual,"CLP")
    condicional = 1
elif ingreso < 80000:
    pie = (casa * 0.30)
    mensual = (casa - pie)/84
    print("Por el concepto de pie el comprador debe pagar: ",pie,"CLP")
    print("Cada mensualidad a pagar por 10 años saldrian cada una a: ",mensual,"CLP")
    condicional = 1
else:
    print("El ingreso del comprador no es valido para la empresa")
    ingreso = int(input("Ingrese el ingreso del comprador: "))
"""