

nome = input('Digite o seu nome >> ')
execucao = ['Repetir Número', 'verifcar lista de compra e adicionar', 'verificar relevancia']

opcao = int(input('Digite alguma Opção \n 0-[Repetir Número] \n 1-[verifcar lista de compra e adicionar] \n 2-[verificar relevancia]\n Opção:  '))
if opcao == 0:
    numero =int( input('digite um número para contar: '))
    i = list(range(0,numero))
    for n in i:
     print('Contando ', n)

elif opcao==1:
   print("verificando", 6*'..')
   listaCompra=['Arroz','Fijão','Açucar','Fuba','Massa']
   print(listaCompra)
   op = input("Deseja adicionar [sim-Sim-s-S]: ")
   if op == 'sim' or 'Sim' or 's' or 'S':
      item = input('O que deseja adicionar? \n')
      listaCompra.append(item)
      print('Lista final : ', listaCompra)
   else:
        print('Sm opção......')
        

elif opcao == 2:
   print('Deseja saber se és menor ,você veio no loal certo!')
   idade  = int(input(f'Digite a sua idade {nome}'))
   if idade <=17:
      print(f'Infelizmente tú és menor de idade, {idade} é muito pouco')
      print(f'Relaxa e cresce mais {nome}')
   else:
     print(f'Parabéns tú és maior de idade, {idade} está bo para ser militar kkkk')
     print(f'Relaxa estava a brincar  cresce mais {nome}')
else:
   print(f' {opcao} não corresponde as opções propostas a cima')
