
# Devmos ter atenção nos atributos da class principal devem ser os mesmo que a filho herança herdar semão haverá erro
class Carro:
    def __init__(self,cor,modelo):
     self.cor = cor
     self.modelo = modelo
        
    def descricao(self):
        print(f"Hola eu su um carro com a cor {self.cor} ")
        print(f"Meu modelo é modelo {self.modelo}")


            #APLICANDO A HERANÇA

class Heranca(Carro):
      def __init__(self,cor,modelo):
            super().__init__(cor,modelo)
        

carro1 = Heranca('Preto','Porche')
print(carro1.descricao())
