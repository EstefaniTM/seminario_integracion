"""
pide salario y desempeno (1-5)
si el desempeño es:
>4 = 15%
>3=10%
>2=5%
>1=2%
"""

salario = int(input("Ingrese el salario: "))
desempenio = int(input("Ingrese el desempeño"))

if(desempenio>4):
    var = salario * 15 / 100
    print(desempenio)
elif(desempenio>3):
    var = salario * 10 / 100
    print(var)
elif(desempenio>2):
    var=salario*5/100
    print(var)
elif(desempenio>1):
    var=salario*2/100
    print(var)