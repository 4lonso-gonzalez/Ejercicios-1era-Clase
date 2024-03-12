# Ejercicio 1
edad = int(input("Edad del cliente: "))
asiento = int(input("Precio unico de los asientos: "))

#Opción 1:
"""
if 5<= edad <=14:
    print("El valor del asiento seria de:",(asiento-(asiento * 0.35)),"CLP")
elif 15<= edad <=19:
    print("El valor del asiento seria de:",(asiento-(asiento * 0.25)),"CLP")
elif 20<= edad <=45:
    print("El valor del asiento seria de:",(asiento-(asiento * 0.10)),"CLP")
elif 46<= edad <=65:
    print("El valor del asiento seria de:",(asiento-(asiento * 0.25)),"CLP")
elif edad >=66:
    print("El valor del asiento seria de:",(asiento-(asiento * 0.35)),"CLP")
else:
    print("El cliente no tiene la edad necesaria")
"""

#Opción 2:
"""
condicional = 0
while condicional == 0:
    if 5<= edad <=14:
        print("El valor del asiento seria de:",(asiento-(asiento * 0.35)),"CLP")
        condicional = 1
    elif 15<= edad <=19:
        print("El valor del asiento seria de:",(asiento-(asiento * 0.25)),"CLP")
        condicional = 1
    elif 20<= edad <=45:
        print("El valor del asiento seria de:",(asiento-(asiento * 0.10)),"CLP")
        condicional = 1
    elif 46<= edad <=65:
        print("El valor del asiento seria de:",(asiento-(asiento * 0.25)),"CLP")
        condicional = 1
    elif edad >=66:
        print("El valor del asiento seria de:",(asiento-(asiento * 0.35)),"CLP")
        condicional = 1
    else:
        print("El cliente no tiene la edad necesaria")
        edad = int(input("Edad del cliente: "))
"""