import pandas as pd

# Carregar a planilha Excel
df = pd.read_excel('C:/Users/gabar/Downloads/Pasta1.xlsx')

# Exibir as primeiras linhas do DataFrame para inspecionar a estrutura e identificar a coluna alvo
print(df.head())

# Suponha que a coluna alvo é 'Nome_da_Coluna_Alvo' (substitua pelo nome real da coluna)
coluna_alvo = 'Unnamed: 1'

# Identificar linhas duplicadas na coluna alvo
duplicados = df[df.duplicated(coluna_alvo, keep=False)]

# Exibir os valores duplicados
print(duplicados)

# Salvar os dados duplicados em um novo arquivo Excel
duplicados.to_excel('C:/Users/gabar/Downloads/duplicados.xlsx', index=False)
