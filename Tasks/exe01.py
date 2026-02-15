"""1- O volume	de	uma	esfera	com	raio	r É 4/3*PI DE EXPOENTE R AO QUADRADO	
.	Qual	é	o	volume	de	uma	esfera	com	raio"""
import math

print("======"*24)
print("======"*24)

nome = str(input("Digite o seu nome por favor: "))

entrada = int(input("Digite 1 para calcular o valor do Raio , 0 sair: "))

if entrada == 1:        
    print(f"SEJA BEM-VINDO AO MINI CALCULO {nome}")
    raio = int(input("Digite o valor do Raio: "))
    volume_esfera = ((4/3)*1.1415)*(math.pow(raio,3))
    print(volume_esfera)
elif entrada == 0:
    print("Saindo...................")
    print("Saiu")
else:
    print("entrada não definida")

print("======"*24)
print("======"*24)
