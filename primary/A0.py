for i in range(1,100):
    if i%2==0:
        print(f" numero par {i}")
    elif i%2==1:
        print(f"numero impar {i}")


def saudar(sad):
    print(f" Hola {sad}")

saudar('samuel')

def somar(a,b):
    return a+b
res = somar(33,44)
print(f"a soma é {res}")
