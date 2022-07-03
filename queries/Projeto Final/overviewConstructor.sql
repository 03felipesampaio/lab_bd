SELECT COUNT(*) as qtd_vitorias FROM results WHERE position=1 AND constructorid=1;
SELECT COUNT(DISTINCT(driverid)) qtd_pilotos FROM results WHERE constructorid=1;
SELECT MIN(RA.year) prim_ano, MAX(RA.year) ult_ano FROM results JOIN races RA USING (raceid)	WHERE constructorid=1;