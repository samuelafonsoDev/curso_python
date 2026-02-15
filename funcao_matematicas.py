import math # Sempre que for para usar uma função matematica importamos o math

print(math)
# SAIDA ==> <module 'math' (built-in)>
som_maior = int(input("digite valor do som maior para calcular proporçao do sinal em decibeis"))
som_menor = int(input("digite valor do som menor para calcular proporçao do sinal em decibeis"))

radio = som_maior/som_menor
decibel = 10 * math.log10(radio)

print(f"O valor calculado é {radio}")
print(math.sin(radio))
print(math.pi)

w = 4
x = math.exp(math.log(w+1))
print( x)