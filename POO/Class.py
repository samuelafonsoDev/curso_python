class Carro:

    """Estamos a definir uma classe e dentro dela temos alguns argumetos básicos"""
    carro1 ='JETUR BLACK'
    carro2 = 'V8 BLACK'
carro = Carro()

print(Carro.carro1)
print(type(carro))


class Pessoa:
    def saudar(self): # Metodos
        print("EXECUTANDO O METODO DA CLASS PESSOA")

samuel  = Pessoa()
print(samuel.saudar())