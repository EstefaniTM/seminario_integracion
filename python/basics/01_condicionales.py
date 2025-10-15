"""
Escribe un programa que pida edad, años de experiencia y si tiene titulo universitario
Un candidato es elegible si tiene >=21 años y experiencia >=2 años o titulo.
Muestra Elegible o No elegible
"""

edad = int(input("Edad del candidato"))
exp = float(input("Anios de experiencia"))
tiene_titulo = input("Tiene titulo universitario? s/n").strip().lower()=="s"

if (edad>=21 and (exp>=2 or tiene_titulo=="s")):
    print("Elegible")
else:
    print("No Elegible")