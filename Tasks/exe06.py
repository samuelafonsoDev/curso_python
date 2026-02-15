"""
Docstring for Tasks.exe06
Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam 
imposto pessoas cujo salário é maior que R$ 1.200,00.
"""
nome = input("Digite o seu nome: ")

salario = int(input("digite o seu salario: "))
if salario>1200:
    print(f"Parabéns {nome} você já pode pagar imposto")
else:
    print(f"Ops {nome} você ainda não pode pagar imposto")
