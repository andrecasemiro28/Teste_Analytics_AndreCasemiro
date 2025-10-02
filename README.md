# Teste_Analytics_AndreCasemiro



Geração do Dataset
Criação do DataFrame: Um DataFrame com 60 registros é gerado para garantir que, mesmo após a limpeza, reste um volume de dados significativo.

Introdução de Problemas: De forma proposital, o script insere valores nulos (NaN) e duplica registros para simular um cenário real onde os dados brutos não são perfeitos.

Limpeza dos Dados
Tratamento de Nulos: Valores faltantes na coluna Quantidade são preenchidos com a mediana, uma abordagem robusta. Linhas com Preço faltante são removidas, pois esta é uma informação crítica para a análise.

Remoção de Duplicatas: O método .drop_duplicates() é utilizado para remover todas as linhas que são cópias exatas de outras.

Conversão de Tipos: Garante que a coluna Data seja do tipo datetime (essencial para análises temporais), Quantidade seja um número inteiro e Preço um número de ponto flutuante (float).

Salvando o Arquivo
O DataFrame limpo e processado é salvo no arquivo data_clean.csv. O uso de ; como separador e , como decimal é um padrão comum em regiões que utilizam o português.

Análise dos Dados
Cálculo do Faturamento: Uma nova coluna, Total Vendas, é criada a partir da multiplicação da Quantidade pelo Preço de cada transação.

Agrupamento: A função .groupby('Produto') é usada para agrupar todas as transações pelo nome do produto.

Soma e Ordenação: O método .sum() calcula o faturamento total para cada grupo (produto), e .sort_values(ascending=False) ordena os produtos do maior para o menor faturamento.

Identificação do Melhor Produto: Por fim, .idxmax() encontra o nome do produto que corresponde ao valor máximo de faturamento na série de vendas.
