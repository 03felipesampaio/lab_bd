-- Quantidades de vitorias da escuderia
SELECT COUNT(*) as qtd_vitorias
    FROM results 
    WHERE position = 1 
        AND constructorid = 1;


-- Numero de pilotos que ja correram pela escuderia
SELECT COUNT( DISTINCT(driverid) ) qtd_pilotos 
    FROM results
    WHERE constructorid = 1;


-- Primeiro e ultimo ano de registros de corridas pela escuderia
SELECT
        MIN(RA.year) prim_ano,
        MAX(RA.year) ult_ano 
    FROM results 
    JOIN races RA USING (raceid)
    WHERE constructorid = 1;