# Nesta etapa a função sera mostrar elementos de uma lista por posição

linguagens = ['PYTHON','JAVASCRIPT', 'GO', 'PHP', 'RUST', 'C++']

print(linguagens[1:])

"""
Quando colocamos só [0 ou 1 ou 2.....] ele mostra o item em função a posição da lista
Agora quando colocamos somente [1:xxx] ele vai pensar assim:
    da posição 1 para frente mostra todos os ites.
    ele faz assim primeiro conta a lista por posição normal em -1 [x:]
    depois o ouro elemento ele conta a lista em 1 sem subtrair 
"""
# Agora vamos aplicar o for com fatiação de lista

for l in linguagens[1:4]:
    print(l)