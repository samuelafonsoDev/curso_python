carros =['ferrari','bulgari','lamborguine']

for carro in carros:
    print(f'Eu comprei um super carrão do modélo: '+ carro)


#trabalhando com for percorrendo tupla]

numeros = list(range(0,101))

for n in numeros:
    print('chegou o número: ',n)


#Trabalhando com a função Range
print("======"*32)
valor = []
for cont in range(2,22):
    print( 'Range conta ', cont)
    valor.append(cont)

print('Depois da repetição o valor foi adiconado a uma lista ',valor)