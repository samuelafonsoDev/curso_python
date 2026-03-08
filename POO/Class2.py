class Animal:

    def __init__(self,nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f'Woooo eu estou latidondo, e me chamo {self.nome}')
        print(f'A minha raça é {self.raca} e tenho {self.idade} de idade ')

animal1  = Animal(nome="Max",raca='Pastor Alemão', idade=int(2))
print(animal1.latir())
