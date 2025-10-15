"""
Pide el numero de empleados y luego el sueldo de cada uno.
suma y muestra la nomina total
"""

empleados = int(input("Ingrese el numero de empleados: "))
resultado = 0
for empleado in range(0, empleados):
    resultado += int(input("Ingrese el salario de empleado: "))
    
print("Total: ", resultado)