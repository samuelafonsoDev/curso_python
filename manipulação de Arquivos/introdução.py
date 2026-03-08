
#POR PADRÃO TUDO ESCRITO EM UM ARQUIVO É STRING, ENTÃO QUER QUIZERMOS PASSAR UM NUMER TEMOS DE CONVERTE ELE EM STRING STR()
arquivo = open("introducao.txt", 'w')# Aqui estamos a abrir um arquivo de nome introduçao, caso tenha ele vai apagar e criar o mesmo de novo, caso não ele vai criar um novo
texto = "Introducoo a escrita com manipulacao de arquivos com python"  # texto que vamos inserir no arquivo, pode ser amrzenado em uma variavel
number = 1234
arquivo.write(str(number))

arquivo.close()

try:
    find = open('ba.txt')
except:
    print('Arquivo não encontrado')
