import math
def apresentacao():
    print("Holla eu sou o fulano e estou aprendendo python")

apresentacao()
print("REPITINDO ", "====="*20)
# Nós podemos juntar função uma dentro de outra para alcançar algum objectivo
def repetir_apresentacao():
            apresentacao()
            apresentacao()
            print("calculo de potencia: ", math.pow(2,3))

repetir_apresentacao()
#============================ARGUMENTOS=====================

print("ARGUMENTOS", "======"*24)

def argumentos(val): # Tmbém podemos usar uma varial como argumento de uma função
     print(val)

argumentos('Samuel como argumento string')

print("==="*24)
print("Argumento por variavel existente  definida na função")

variavel = 'Samuel está aprender python '
# Crie uma variavel e adiciona como argumento de uma função, também funciona
argumentos(variavel)

"""
Quando	você	cria	uma	variável	dentro	de	uma	função,	ela	é	local,	ou	seja,	ela	só	existe
dentro	da	função.	Por	exemplo:

    def	cat_twice(part1,	part2):
    cat	=	part1	+	part2
    
print_twice(cat)
"""