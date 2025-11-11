# Programa que insere asteriscos (*) entre as letras de um nome

# Define o nome a ser processado
nome = input(f'Digite o seu nome: ')

# Calcula o tamanho do nome (número de caracteres)
tam_nome = len(nome)

# Cria uma string vazia que vai receber o novo nome formatado
novo_nome = ''

# Variável de controle para o loop
letra = 0

# Loop que percorre cada posição (índice) do nome
while letra < tam_nome:
    # Adiciona um asterisco antes de cada letra
    novo_nome += f'*{nome[letra]}'
    # Incrementa o índice para passar à próxima letra
    letra += 1

# Adiciona o último asterisco no final
novo_nome += '*'

# Exibe o resultado final
print(f'Nome formatado: {novo_nome}')
