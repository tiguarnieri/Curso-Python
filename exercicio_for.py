import os

# Jogo de adivinhação de palavra (estilo forca simples)

# Palavra secreta que o jogador deve descobrir
pal_secreta = input(f'Primeiro jogador, digite qual palavra deseja que o segundo jogador descubra: ').lower()

# Contador de tentativas erradas
tentativas = int(0)

# Armazena as letras que o jogador já acertou
letras_certas = ''

# Cria uma lista com * no lugar de cada letra da palavra
pal_descoberta = ['*' for letras in pal_secreta]


# O jogo continua enquanto o número de letras certas for menor que o total da palavra
while len(letras_certas) < len(pal_secreta):

    # Solicita uma letra do jogador e converte para minúscula
    letra = input('Digite uma letra: ').lower()

    # Impede que o jogador digite mais de uma letra por vez
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    # Verifica se a letra está na palavra secreta
    if letra in pal_secreta:
        if letra in letras_certas:
            print(f'Você já acertou a letra {letra.upper()}. Tente outra.')
            continue
        # Percorre cada posição da palavra
        for letras in range(len(pal_secreta)):
            # Se a letra digitada for igual à letra da posição atual
            if letra == pal_secreta[letras]:
                # Substitui o * pela letra correta
                pal_descoberta[letras] = letra
                # Adiciona a letra ao registro de acertos
                letras_certas += letra
                # Informa que o jogador acertou a letra
                print(f"Você acertou a letra!")
    # Caso a letra não esteja na palavra
    else:
        tentativas += 1
        print(f'Você errou, tente novamente. Tentativas: {tentativas}')
        

     # Mostra a palavra parcialmente descoberta
    print(f"A palavra é {' '.join(pal_descoberta).upper()}")

os.system('cls') # Limpa a tela para uma melhor visualização

# Quando todas as letras forem descobertas, o jogo termina
print(f'\nParabéns, você descobriu a palavra secreta: {pal_secreta.upper()}')
print(f'Você errou {tentativas} letras.')