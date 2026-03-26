
caso = input("Digite [1-Verficar se é um numero]: ")

try:
        number = int(input("Digite um valor inteiro: "))
        print(f" Valor digitado é {number}")
except:
        print(" O código exigido era um valor inteiro e você errou ao digitar um valor do tip String")
finally:
        print("Código executado com sucesso do sector [1]")

    

