""" FOR Comando for será muito utilizado quando quizermos
trabalhar com um laço de repetição onde CONHECEMOS O SEU LIMITE,
ou seja, quando temos um objeto em forma de lista ou
dicionário e queremos que uma variável percorra cada elemento
dessa lista/dicionário interagindo com o mesmo"""


compras = ['CPU','MONITOR','PLACA GRÁFICA']

for item in compras:
    print(item)

# A contagem de range sempre dimimui um no fim (A,B) A inicio da contagem e B o fim , ele passa para cada elemento
for x in range(6):
    print(x)


nomes = ['Samuel','Joseane','Cássia']

for n in nomes:
    print(n)

else:
    print("=======Fim do Laço========")

#EXECERCICIOS DA TABUADA

for x in range(13):
    for y in range(13):
        print(f'{x}*{y}  = {x*y}')