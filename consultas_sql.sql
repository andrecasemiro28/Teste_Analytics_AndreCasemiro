-- =======================================================================================
-- CONSULTA 1: Listar o total de vendas por produto
-- =======================================================================================
-- OBJETIVO:
-- Calcular o faturamento total para cada produto, listando o nome do produto,
-- sua categoria e o valor total das vendas. O resultado deve ser ordenado do produto
-- que mais vendeu para o que menos vendeu.

-- LÓGICA:
-- 1. SELECT Produto, Categoria: Seleciona as colunas que queremos agrupar.
-- 2. SUM(Quantidade * Preco) AS TotalVendas: Calcula o faturamento total multiplicando
--    a quantidade pelo preço para cada venda e depois soma esses valores para cada grupo
--    de produtos. O resultado é nomeado como 'TotalVendas'.
-- 3. FROM Vendas: Especifica que estamos consultando a tabela 'Vendas'.
-- 4. GROUP BY Produto, Categoria: Agrupa todas as linhas que têm o mesmo nome de produto
--    e categoria, para que a função SUM() calcule o total para cada produto distinto.
-- 5. ORDER BY TotalVendas DESC: Ordena os resultados com base na coluna calculada
--    'TotalVendas', em ordem decrescente (do maior para o menor).

SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS TotalVendas
FROM
    Vendas
GROUP BY
    Produto,
    Categoria
ORDER BY
    TotalVendas DESC;

-- =======================================================================================
-- CONSULTA 2: Identificar os produtos menos vendidos em um mês específico
-- =======================================================================================
-- OBJETIVO:
-- Listar os produtos que tiveram a menor quantidade de unidades vendidas durante
-- o mês de junho.

-- NOTA IMPORTANTE:
-- O dataset fornecido contém dados apenas para o ano de 2023. A consulta foi adaptada
-- para buscar os dados de Junho de 2023, em vez de 2024.

-- LÓGICA:
-- 1. SELECT Produto, SUM(Quantidade) AS QuantidadeTotalVendida: Seleciona o nome do
--    produto e calcula a soma total de unidades vendidas para cada um, nomeando
--    a coluna como 'QuantidadeTotalVendida'.
-- 2. FROM Vendas: Especifica a tabela de origem.
-- 3. WHERE strftime('%Y-%m', Data) = '2023-06': Filtra a tabela para incluir apenas
--    os registros do ano de 2023 e mês 06 (Junho). A função strftime() é usada aqui
--    (comum em SQLite), mas pode variar em outros bancos de dados (ex: `FORMAT(Data, 'yyyy-MM')`
--    no SQL Server ou `DATE_FORMAT(Data, '%Y-%m')` no MySQL).
-- 4. GROUP BY Produto: Agrupa os registros por produto para que a soma da quantidade
--    seja calculada corretamente para cada um.
-- 5. ORDER BY QuantidadeTotalVendida ASC: Ordena os produtos com base na quantidade
--    total vendida, em ordem ascendente (do menor para o maior), para que os menos
--    vendidos apareçam primeiro.

SELECT
    Produto,
    SUM(Quantidade) AS QuantidadeTotalVendida
FROM
    Vendas
WHERE
    strftime('%Y-%m', Data) = '2023-06' -- Adaptado para Junho de 2023, pois o dataset é de 2023.
GROUP BY
    Produto
ORDER BY
    QuantidadeTotalVendida ASC;