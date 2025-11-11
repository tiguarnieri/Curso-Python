nome = 'Tiago'
tam_nome = len(nome)
novo_nome = ''
letra = 0

while letra < tam_nome:
    novo_nome += f'*{nome[letra]}'
    letra += 1

novo_nome += '*'
print (novo_nome)