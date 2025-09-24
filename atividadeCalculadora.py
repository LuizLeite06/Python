Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))

Somar = 1
Subtrair = 2
Multiplicar = 3
Dividir = 4

op = int(input("Digite de 1 a 4 para somar, subtrair, multipicar e dividir: "))

if op <=1:
    print(Num1 + Num2)

elif op <=2:
    print(Num1 - Num2) 

elif op <=3:
    print(Num1 * Num2) 


elif op <=4:
    print(Num1 / Num2 )

else:
    print("Você nao digitou um numero valido")    







