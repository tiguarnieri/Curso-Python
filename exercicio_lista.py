import os  # Importa o módulo 'os' para usar comandos do sistema operacional (como limpar a tela)

lista = []  # Cria uma lista vazia para armazenar os valores inseridos
opcao = ''  # Variável que guardará a opção digitada pelo usuário

# Loop principal do programa — roda até que o usuário escolha sair
while True:
    print(f'Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air\n').lower()  # Lê a opção e converte para minúscula

    # --- Inserir item ---
    if opcao == 'i':
        os.system('cls')  # Limpa a tela (no Windows)
        valor = input(f'Valor: ')  # Solicita o valor a ser inserido
        os.system('cls')  # Limpa novamente para deixar a tela limpa
        lista.append(valor)  # Adiciona o valor à lista
        print(f'Lista atual: {lista}\n')  # Mostra a lista atualizada

    # --- Listar itens ---
    elif opcao == 'l':
        os.system('cls')
        # 'enumerate' retorna o índice e o valor de cada item na lista
        for i, valor in enumerate(lista):
            print(f'{i} - {valor}')  # Exibe o índice e o valor

    # --- Apagar item pelo índice ---
    elif opcao == 'a':
        os.system('cls')
        indice = input(f'Qual o indice a ser apagado: ').lower()  # Lê o índice a ser removido
        os.system('cls')
        try:
            indice = int(indice)  # Converte o valor para inteiro
            del lista[indice]  # Apaga o item pelo índice
            print(f'Lista atual: {lista}\n')
        except:
            # Se o índice não for um número ou estiver fora do intervalo da lista
            os.system('cls')
            print('Indice invalido ou fora do intervalo\n')

    # --- Sair do programa ---
    elif opcao == 's':
        os.system('cls')
        print('Saindo...\n')
        break  # Encerra o loop e o programa

    # --- Opção inválida ---
    else:
        os.system('cls')
        print('Opção invalida\n')