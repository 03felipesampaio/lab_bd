SELECT S.status, COUNT(*) Resultados from results R
	JOIN status S USING(statusid)
	GROUP BY S.statusid
	ORDER BY S.status;