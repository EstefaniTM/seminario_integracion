"""
sistema que pida pago por hora y horas trabajadas las primeras 40
horas son normales, las extras se pagan al 150%
calcula y muestra el total semanal
"""
pago_hora = float(input("Ingrese el pago por hora: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

if horas_trabajadas <=40:
    total_semana = pago_hora * horas_trabajadas
else:
    horas_trabajadas= horas_trabajadas -40
    total_semana = (pago_hora * 40) +(pago_hora * 1.5 * horas_trabajadas)
print(f"el total de la semana es ${total_semana}")

