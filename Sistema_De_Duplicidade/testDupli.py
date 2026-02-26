import pandas as pd

# Carregar a planilha Excel
df = pd.read_excel('C:/Users/gabar/Downloads/Pasta1.xlsx')

# Identificar linhas duplicadas na coluna 'Coluna_Alvo'
duplicados = df[df.duplicated('Unnamed: 1', keep=False)]

# Exibir os valores duplicados
print(duplicados)

# Salvar os dados duplicados em um novo arquivo Excel
duplicados.to_excel('C:/Users/gabar/Downloads/duplicados.xlsx', index=False)
