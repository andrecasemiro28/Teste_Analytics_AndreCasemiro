import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

# --- 1. Carregamento e Preparação dos Dados ---
# Bloco de segurança para garantir que o arquivo exista
try:
    # Carrega o dataset, especificando o separador ';' e o decimal ','
    df = pd.read_csv('data_clean.csv', sep=';', decimal=',')
    print("Arquivo 'data_clean.csv' carregado com sucesso.")
except FileNotFoundError:
    print("ERRO: O arquivo 'data_clean.csv' não foi encontrado.")
    print("Por favor, certifique-se de que o arquivo está no mesmo diretório que o script.")
    exit() # Encerra o script se o arquivo não for encontrado

# --- 2. Tratamento e Criação de Novas Colunas ---
# Garante que a coluna 'Data' seja do tipo datetime para análises temporais
# Specify the correct date format as "dd/mm/yyyy"
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Calcula o faturamento de cada transação
df['Total Vendas'] = df['Quantidade'] * df['Preço']

# --- 3. Análise e Gráfico: Tendência de Vendas Mensais ---
# Define a coluna 'Data' como índice para facilitar o agrupamento por tempo
df_indexed = df.set_index('Data')

# Agrupa as vendas por mês ('ME' = Month End) e soma os totais
vendas_mensais = df_indexed['Total Vendas'].resample('ME').sum()

# --- Criação do Gráfico de Linha ---
plt.figure(figsize=(12, 7))
plt.plot(vendas_mensais.index, vendas_mensais.values, marker='o', linestyle='-', color='#007ACC')

# Títulos e Rótulos
plt.title('Tendência de Vendas Mensais (2023)', fontsize=16, weight='bold')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Formatação do eixo Y para moeda (Real)
formatter_currency = mticker.FuncFormatter(lambda x, p: f'R$ {x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter_currency)

# Formatação do eixo X para exibir meses de forma clara
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, ha='right')
plt.tight_layout() # Ajusta o gráfico para evitar sobreposição

# Salva a imagem do gráfico
plt.savefig('tendencia_vendas_mensal.png')
print("Gráfico de tendência de vendas salvo como 'tendencia_vendas_mensal.png'")


# --- 4. Análise e Gráfico: Vendas por Categoria ---
# Agrupa o faturamento total por categoria de produto
vendas_por_categoria = df.groupby('Categoria')['Total Vendas'].sum().sort_values(ascending=False)

# --- Criação do Gráfico de Barras ---
plt.figure(figsize=(10, 6))
bars = vendas_por_categoria.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Títulos e Rótulos
plt.title('Total de Vendas por Categoria de Produto', fontsize=16, weight='bold')
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=0) # Mantém os nomes das categorias na horizontal

# Formatação do eixo Y
plt.gca().yaxis.set_major_formatter(formatter_currency)

# Adiciona os rótulos de valor em cima de cada barra
for bar in bars.patches:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'R$ {yval:,.0f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()

# Salva a imagem do gráfico
plt.savefig('vendas_por_categoria.png')
print("Gráfico de vendas por categoria salvo como 'vendas_por_categoria.png'")

# Exibe os gráficos (opcional, pode ser desativado se rodar como script)
plt.show()

















