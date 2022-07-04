SELECT RA.name nome, CAST(RA.YEAR AS VARCHAR(4)) ano, COUNT(*) vitorias
	FROM results R
	JOIN races RA USING(raceid)
	WHERE R.position = 1 AND R.driverid = 1
	GROUP BY ROLLUP(RA.year, RA.name)
	ORDER BY RA.year DESC, count(*)  DESC;