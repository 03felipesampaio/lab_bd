-- Quantidade de vitorias do piloto
SELECT COUNT(*) qtd_vitorias 
    FROM results
    WHERE position = 1 
        AND driverid = 1;

-- Primeiro e ultimo ano de corrida do piloto
SELECT 
        MIN(RA.year) prim_ano, 
        MAX(RA.year) ult_ano 
    FROM results 
    JOIN races RA USING (raceid)
    WHERE driverid=1;