"""
Armazenam coleções de objetos heterogêneos
Crescem até o limite da memória
vetores, matrizes, registros e listas encadeadas
Acesso sequencial, em fatias ou direto por índice
Implementadas com arrays
Possuem diversos métodos: adicionar, remover, ordenar,
procurar, contar
Listas são mutáveis e tuplas são imutáveis
Listas são delimitadas por [ e ] 

[ ] [ ]

"""

lista = [98, ["samuel",123,True],"Sara"]
# APEND
lista.append("Saaaaa")
print(lista)
# INSERT
lista.insert(4,123445) # O primeiro valor antes da virgula referece a posição
print(lista)

lista.reverse() # Troca do inicio ao fim , para fim ao inicio a ordem.
print(lista)

print(type(lista))
a,b = 0,1
print(b)

a = [1,2,3,4]

