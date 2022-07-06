-- Cria indice para identificacao de vencedores
CREATE INDEX IF NOT EXISTS wins_construc ON results(driverid, constructorid) WHERE position = 1;

-- Listagem do pilotos e vitorias pela escuderia
SELECT D.forename "Nome", D.surname "Sobrenome", COUNT(*) "Vitórias"
	FROM results R
	JOIN driver D USING (driverid)
	WHERE R."position" = 1 AND R.constructorid = 1
	GROUP BY D.driverid
	ORDER BY COUNT(*) DESC;