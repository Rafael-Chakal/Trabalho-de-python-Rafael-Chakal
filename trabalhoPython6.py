#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

num = float(input("\nDigite um número: "))

if (num == round(num)):

    print(int(num),"é um número inteiro!")

else:

    print(num,"é um número decimal!")