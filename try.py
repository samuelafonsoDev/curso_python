a = [1,2,3,4]

try:
    p = int(input("digite a posição: "))
    print(a[p])
except IndexError:
    print("posição nula")
finally:
    print("programa finalizado")