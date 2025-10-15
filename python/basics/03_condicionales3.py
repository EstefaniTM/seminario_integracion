"""
Vacaciones por antiguedad 
Pide años de antiguedad y muestra dias de vacaciones segun 
<1=0
<3=3
<5=10
>=5=15
"""

aniosAntiguedad = int(input("Ingrese los anios por antiguedad: "))

if (aniosAntiguedad<1):
    print("Tiene 0 dias de vacaciones")
elif (aniosAntiguedad<3):
    print("Tiene 3 dias de vacaciones")
elif(aniosAntiguedad<5):
    print("Tiene 10 dias de vacaciones")
elif(aniosAntiguedad>=15):
    print("Tiene 15 dias de vacasiones")
else:
    print("error")