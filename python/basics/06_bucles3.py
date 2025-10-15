"""
pide numero de ekmpleados cada empleado solicita nombre y salario determina quien.
 tiene el mayor salario y muestralo

"""

num_empleados = int(input("Ingrese el número de empleados: "))

lista = []

i = 1  

while i <= num_empleados:
    nombre = input(f"Ingrese el nombre del empleado {i}: ")
    sueldo = float(input(f"Ingrese el salario de {nombre}: "))
    lista.append((nombre, sueldo)) 
    i += 1

mayor_empleado = max(lista, key=lambda x: x[1]) 

print(f"El empleado con mayor salario es {mayor_empleado[0]} con {mayor_empleado[1]}")

