# Declaração de variáveis básicas
nome = 'Tiago'                # Nome da pessoa
sobrenome = 'Guarnieri'       # Sobrenome da pessoa
idade = 37                    # Idade atual
ano_nascimento = 2025 - idade # Cálculo do ano de nascimento com base no ano atual (2025)
maior_de_idade = (idade >= 18) # Verifica se a pessoa é maior de idade (True ou False)
altura_metros = 1.81          # Altura em metros

# Exibição das informações formatadas no console
print(
    'Meu nome é', nome, sobrenome,
    ', tenho', idade,
    'anos, nasci no ano de', ano_nascimento,
    ', tenho', altura_metros, 'm',
    'e se sou maior de idade:', maior_de_idade
)

# Linha em branco no final (apenas para espaçamento visual)
print('\n')