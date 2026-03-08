"""
arquivo = open('texto.txt','r')

for linha in arquivo:
    print(linha)

arquivo.close()
"""
with open('texto.txt','w') as  arquivo:
    arquivo.write('Olá Mundo')

nome = "Samuel"
print(nome.title())
