"""
elementos fundametais para operaçãoAritmetrica

* multiplicação
/ divisão
+ adicção
- subtração
% mod resto da divisão
** potencia

"""


n = int(input("Digite o seu numero: "));
if n%2==0:
    print(f" número Par {n}");
    resp = input(f"Deseja saber a potencia de base 2 de {n} digite S (sim) ou N (não)" )
    
    if resp == "S":
        potenc = n**2
        print(f" A pontência de base 2 de {n} é {potenc}");
        print(4*"====")
    elif resp == "N":
        print("Vc não escolheu ver a potencia")
else:
    print("Impar");
    print(4*"--------");



