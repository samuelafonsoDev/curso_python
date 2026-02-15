"""
Docstring for Tasks.exe03
03) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor 
correspondente em graus Celsius (baseado na fórmula abaixo): 
"""

C = float(input("Digite a temperatura em °C:"))
F = (9*C/5)+32
print("%5.2f°C é igual a %5.2f°F" % (C, F))