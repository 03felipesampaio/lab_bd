SELECT S.status, COUNT(*) Resultados from results R
	JOIN status S USING(statusid)
	WHERE R.constructorid=1
	GROUP BY S.statusid
	ORDER BY COUNT(*) DESC;