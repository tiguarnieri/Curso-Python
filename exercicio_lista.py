lista = []
opcao = ''

while True:
    print(f'Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar ')

    if opcao == 'i':
        valor = input(f'Valor: ')
        lista.append(valor)
    elif opcao == 'l':
        print(lista)
    elif opcao == 'a':
        indice = input(f'Qual o indice a ser apagado: ')
        indice_int = int(indice)
        lista.pop(indice)

    else:
        print('Opção invalida')