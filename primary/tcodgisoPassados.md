# Tipos de dados em python
##
number = 12
leter = "Samuel"
logic = True
real = 12.5
lista = [12, "sra", 0, "sara"]
tupla = (12, 23, 26)
dicionariio = {"nome": "Samuel", "idade": 19, "tipo": True}
letersWithSet = set("Python")
print(type(dicionariio["tipo"]))
print(type(real))
num = int(input("Digite um número: "))
print(num % 2 == 0)
##
n = input("digite o seu nome: ")
v = int(input("digite a sua idade: "))
if v >= 18:
    print(f"Olha {n} tú já és maior de idade tens {v} anos")
elif v < 18:
    print(f" olha {n} tú ainda és menor de idade {v} anos")
else:
    print(f"Idoso {v}")
