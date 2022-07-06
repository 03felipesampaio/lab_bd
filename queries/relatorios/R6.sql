-- Status na carreira do piloto
SELECT S.status, COUNT(*) Resultados from results R
	JOIN status S USING(statusid)
	WHERE R.driverid = 1
	GROUP BY S.statusid
	ORDER BY S.status;