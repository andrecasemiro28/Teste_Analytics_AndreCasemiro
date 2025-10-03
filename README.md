# Teste_Analytics_AndreCasemiro


Análise de Vendas com Python e Pandas
📜 Descrição
Este projeto consiste em um script Python que simula, limpa e analisa um conjunto de dados de vendas. O objetivo é demonstrar um fluxo de trabalho básico de análise de dados, desde a geração de dados brutos até a extração de insights acionáveis, como a identificação do produto mais rentável.

✨ Funcionalidades
Geração de Dados: Cria um dataset de vendas com dados realistas usando a biblioteca Faker.

Simulação de Problemas: Introduz propositalmente dados faltantes (NaN) e registros duplicados para simular um cenário real de ETL (Extração, Transformação e Carga).

Limpeza de Dados (Data Cleaning): Aplica técnicas essenciais para tratar valores nulos, remover duplicatas e garantir a consistência dos tipos de dados.

Análise Exploratória: Calcula o faturamento total por produto e identifica o produto com maior volume de vendas.

Exportação de Resultados: Salva o dataset limpo e pronto para análise em um arquivo CSV (data_clean.csv).

⚙️ Pré-requisitos
Antes de executar o script, certifique-se de ter o Python 3 instalado. Você também precisará das seguintes bibliotecas:

pandas

numpy

faker

Você pode instalar todas as dependências com um único comando:

Bash

pip install pandas numpy faker
🚀 Como Executar
Salve o código do script em um arquivo, por exemplo, analise_vendas.py.

Abra um terminal ou prompt de comando.

Navegue até o diretório onde você salvou o arquivo.

Execute o script com o comando:

Bash

python analise_vendas.py
📊 Saída Esperada
Ao executar o script, você obterá:

No terminal:

Mensagens de status indicando cada etapa do processo.

Uma tabela com o faturamento total por produto, ordenado do maior para o menor.

A identificação clara do produto campeão de vendas.

Total de vendas (R$) por produto:
Laptop Gamer        R$ 225.000,00
Smartphone Pro      R$ 135.000,00
Cadeira Gamer       R$ 52.000,00
Monitor 4K          R$ 44.000,00
...

--- Resultado Final da Análise ---
O produto com o maior faturamento foi: 'Laptop Gamer'
Valor total faturado pelo produto: R$ 225.000,00
Um novo arquivo:

Um arquivo chamado data_clean.csv será criado no mesmo diretório. Este arquivo contém os dados de vendas após todo o processo de limpeza, pronto para ser usado em outras análises ou em ferramentas de visualização.

🛠️ Como o Script Funciona
O script é dividido em quatro etapas principais:

1. Geração do Dataset
Criação do DataFrame: Um DataFrame do pandas com 60 registros é gerado. A biblioteca Faker é utilizada para criar dados realistas, como as datas das vendas.

Introdução de Problemas: Para tornar a simulação mais fiel à realidade, o script insere valores nulos (NaN) em colunas críticas e duplica algumas linhas, criando um "dataset sujo" que precisa de tratamento.

2. Limpeza dos Dados
Tratamento de Nulos: Valores faltantes na coluna Quantidade são preenchidos com a mediana (uma medida estatística robusta a outliers). Linhas onde o Preço é nulo são completamente removidas, pois o preço é uma informação indispensável para a análise de faturamento.

Remoção de Duplicatas: O método .drop_duplicates() é utilizado para identificar e remover todas as linhas que são cópias exatas de outras.

Conversão de Tipos: Garante que cada coluna tenha o tipo de dado correto (datetime para datas, int para quantidades, float para preços), o que otimiza a performance e a precisão das operações matemáticas.

3. Salvando o Arquivo
O DataFrame limpo é salvo no arquivo data_clean.csv. A configuração de ; como separador e , como decimal é um padrão comum para arquivos em português, facilitando a importação em softwares como o Microsoft Excel.

4. Análise dos Dados
Cálculo do Faturamento: Uma nova coluna, Total Vendas, é criada a partir da multiplicação da Quantidade pelo Preço de cada transação.

Agrupamento: A função .groupby('Produto') agrega todas as transações por produto, permitindo calcular métricas consolidadas.

Soma e Ordenação: O método .sum() calcula o faturamento total para cada produto, e .sort_values(ascending=False) os ordena do mais rentável para o menos.

Identificação do Melhor Produto: Por fim, .idxmax() é usado para apontar o nome do produto que corresponde ao maior valor de faturamento, entregando o principal insight da análise.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


# Insights da Analise Exploratoria
Gráfico 1: Tendência de Vendas Mensais ao Longo de 2023
O primeiro gráfico mostra a evolução do faturamento total, mês a mês, ao longo do ano de 2023. Isso nos ajuda a visualizar a sazonalidade e os períodos de maior ou menor atividade comercial.

Gráfico 2: Faturamento por Categoria de Produto
Para obter um insight mais profundo sobre o desempenho, analisei o faturamento total gerado por cada categoria de produto. Este gráfico de barras compara diretamente as categorias, mostrando quais são as mais importantes para o negócio.

Insights e Padrões Observados
Com base nas visualizações, podemos extrair pelo menos dois insights importantes:

Concentração de Vendas no Final do Ano: Analisando o gráfico de tendência mensal, observa-se um pico significativo de vendas nos últimos meses do ano, especialmente em Dezembro. As vendas começam de forma moderada, apresentam uma queda no meio do ano (entre Junho e Julho) e disparam no último trimestre. Este é um padrão clássico de sazonalidade, possivelmente impulsionado por eventos como a Black Friday e as festas de fim de ano, indicando uma ótima janela para campanhas de marketing e reforço de estoque.

Categoria "Eletrônicos" Domina o Faturamento: O gráfico de vendas por categoria deixa claro que os Eletrônicos são, de longe, a categoria mais lucrativa, gerando um faturamento substancialmente maior que Acessórios e Móveis somados. Produtos como "Laptop Gamer" e "Smartphone Pro", que possuem alto valor agregado, são os principais motores desse resultado. Isso sugere que o público da loja tem um forte interesse em produtos de maior tecnologia e valor, sendo este o segmento principal que garante a saúde financeira do negócio.
