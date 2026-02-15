
# Aplicando uma pequena contagem, na maioria das veses tem de ter uma variavel de controle e um IN
for num in range(200):
    print(num)


for letras in 'python': # aqui ele vai trazer cada palavra desta string em colunas
    print(letras)


# DIGITAS UM VALOR E O ALGORITIMOS MOSTRA OS VALORES PARES
number = int(input("digite um valor para contagem: "))
par  = [i for i in range(number) if (i%2)==0]
print(f"par {par}")

