# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
n1 = float(input("Digite o primeiro numero "))
n2 = float(input("Digite o segundo numero"))

operacao = input("Digite a operação: soma, subtração, multiplicação ou divisão ")

if operacao == "soma":
    print(n1+n2)
elif operacao =="subtração":
    print(n1-n2)
if operacao == "multiplicação":
    print(n1*n2)
elif operacao =="divisão":
    print(n1/n2)