#4Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
#respectivo índice. Imprima a idade e a altura na ordem inversa a ordem lida.

idadeAltura = []

for c in range(1,3):
    altura = float(input('Digite sua altura [ex = 1.85 ]  : '))
    idadeAltura.append(altura)
    idade =int(input('Digite sua Idade : '))
    idadeAltura.append(idade)
    idadeAltura.reverse()
print(idadeAltura)