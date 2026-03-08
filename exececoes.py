"""
RATANDO EXCEÇÕES USANDO TRY E EXCEPT

Entretanto, se você colocar esse código num programa em Python e esse erro ocorre,
seu programa para imediatamente com um “Traceback” indicando tal erro. Isso
faz com que os próximos comandos não sejam executados.


"""

"""

tempFahrenheit = input("Digite o valor da temperatura em Fahrenheit\n")
Fahrenheit = float(tempFahrenheit) #AQUI ESTAMOS CONVERTER O VALOR QUE SER[A LIDO.
cel = (Fahrenheit-32.0) * 5.0/9.0
print(f" {tempFahrenheit} em Celsius fica {cel}")

"""
"""Este código está a rodar no conforme, mas se alguém digitar mal o vlor dara erro, nos podemos usar o TRY E EXCEPT
para executar codigos caso haja algum erro no execuçã do programa.
"""
tempFahrenheit = input("Digite o valor da temperatura em Fahrenheit\n")

try:

    Fahrenheit = float(tempFahrenheit) #AQUI ESTAMOS CONVERTER O VALOR QUE SER[A LIDO.
    cel = (Fahrenheit-32.0) * 5.0/9.0
    print(f" {tempFahrenheit} em Celsius fica {cel}")

except:
    print("Por favor digite um número, para execução correta")

