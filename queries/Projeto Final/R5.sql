SELECT RA."name", RA."year", COUNT(*)
	FROM results R
	JOIN races RA USING(raceid)
	WHERE R."position" = 1 AND R.driverid = 1
	GROUP BY ROLLUP(RA."year", RA."name")
	ORDER BY RA."year", RA."name";