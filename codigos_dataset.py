import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime

# ==============================================================================
# 1. GERAÇÃO DO DATASET SIMULADO
# ==============================================================================
print("Iniciando a geração do dataset de vendas...")

# Inicializa o gerador de dados Faker
fake = Faker('pt_BR')

# --- Definição dos Parâmetros da Simulação ---
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
num_registros = 60 # Gerar mais que 50 para ter duplicatas e nulos

# Lista de produtos com suas respectivas categorias e preços base
produtos = {
    'Laptop Gamer': {'Categoria': 'Eletrônicos', 'Preço': 7500.00},
    'Smartphone Pro': {'Categoria': 'Eletrônicos', 'Preço': 4500.00},
    'Fone de Ouvido Bluetooth': {'Categoria': 'Acessórios', 'Preço': 350.00},
    'Monitor 4K': {'Categoria': 'Eletrônicos', 'Preço': 2200.00},
    'Teclado Mecânico': {'Categoria': 'Acessórios', 'Preço': 450.00},
    'Cadeira Gamer': {'Categoria': 'Móveis', 'Preço': 1300.00},
    'Webcam Full HD': {'Categoria': 'Acessórios', 'Preço': 250.00}
}
lista_produtos = list(produtos.keys())

# --- Geração dos Dados ---
vendas_lista = []
for i in range(1, num_registros + 1):
    produto_escolhido = random.choice(lista_produtos)
    vendas_lista.append({
        'ID': 1000 + i,
        'Data': fake.date_between(start_date=start_date, end_date=end_date),
        'Produto': produto_escolhido,
        'Categoria': produtos[produto_escolhido]['Categoria'],
        'Quantidade': random.randint(1, 10),
        'Preço': produtos[produto_escolhido]['Preço']
    })

df_vendas = pd.DataFrame(vendas_lista)

# --- Introdução de Problemas para Limpeza ---
print("Introduzindo valores faltantes e duplicatas para a simulação...")
# Adicionar valores Nulos (NaN)
for _ in range(5):
    row_idx = random.randint(0, len(df_vendas)-1)
    col_idx = random.choice(['Quantidade', 'Preço'])
    df_vendas.loc[row_idx, col_idx] = np.nan

# Adicionar registros duplicados
df_vendas = pd.concat([df_vendas, df_vendas.head(3)], ignore_index=True)

print("\nDataset original (com problemas):")
print(df_vendas.head())
print(f"\nDimensões do dataset original: {df_vendas.shape}")
print("\nVerificando nulos e duplicatas no dataset original...")
print("Valores nulos por coluna:\n", df_vendas.isnull().sum())
print("Total de linhas duplicadas:", df_vendas.duplicated().sum())


# ==============================================================================
# 2. LIMPEZA DOS DADOS
# ==============================================================================
print("\n--- Iniciando a limpeza dos dados ---")

# --- Tratamento de valores faltantes ---
# Para a coluna 'Quantidade', preenchemos com a mediana (mais robusta a outliers)
mediana_quantidade = df_vendas['Quantidade'].median()
df_vendas['Quantidade'].fillna(mediana_quantidade, inplace=True)
print(f"\nValores nulos em 'Quantidade' preenchidos com a mediana: {mediana_quantidade}")

# Linhas que ainda possuem valores nulos (na coluna 'Preço') serão removidas
df_vendas.dropna(inplace=True)
print("Linhas com valores nulos restantes foram removidas.")

# --- Remoção de duplicatas ---
df_vendas.drop_duplicates(inplace=True)
print("Linhas duplicadas foram removidas.")

# --- Conversão de tipos de dados ---
print("\nConvertendo tipos de dados...")
# Converter 'Data' para o tipo datetime
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])
# Converter 'Quantidade' para inteiro (pode ter virado float ao preencher nulos)
df_vendas['Quantidade'] = df_vendas['Quantidade'].astype(int)
# 'Preço' já deve ser float, mas garantimos
df_vendas['Preço'] = df_vendas['Preço'].astype(float)

print("\nTipos de dados após conversão:")
df_vendas.info()

print(f"\nDimensões do dataset após limpeza: {df_vendas.shape}")

# ==============================================================================
# 3. SALVANDO O DATASET LIMPO
# ==============================================================================
try:
    df_vendas.to_csv('data_clean.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
    print("\nDataset limpo salvo com sucesso como 'data_clean.csv'")
except Exception as e:
    print(f"\nOcorreu um erro ao salvar o arquivo: {e}")


# ==============================================================================
# 4. ANÁLISE DO DATASET LIMPO
# ==============================================================================
print("\n--- Iniciando a análise dos dados ---")

# --- Calcular o total de vendas por transação ---
df_vendas['Total Vendas'] = df_vendas['Quantidade'] * df_vendas['Preço']

# --- Calcular o total de vendas por produto ---
vendas_por_produto = df_vendas.groupby('Produto')['Total Vendas'].sum().sort_values(ascending=False)

print("\nTotal de vendas (R$) por produto:")
# Formatando a saída para exibir como moeda
print(vendas_por_produto.map('R$ {:,.2f}'.format))

# --- Identificar o produto com o maior número de vendas totais ---
produto_mais_vendido = vendas_por_produto.idxmax()
valor_maximo = vendas_por_produto.max()

print("\n--- Resultado Final da Análise ---")
print(f"O produto com o maior faturamento foi: '{produto_mais_vendido}'")
print(f"Valor total faturado pelo produto: R$ {valor_maximo:,.2f}")
