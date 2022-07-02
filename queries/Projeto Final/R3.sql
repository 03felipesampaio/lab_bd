CREATE INDEX wins_construc ON results(driverid, constructorid) WHERE position = 1;
-- DROP INDEX wins_construc;

SELECT D.forename "Nome", D.surname "Sobrenome", COUNT(*) "Vitórias"
	FROM results R
	JOIN driver D USING (driverid)
	WHERE R."position" = 1 AND R.constructorid = 1
	GROUP BY D.driverid
	ORDER BY D.forename;