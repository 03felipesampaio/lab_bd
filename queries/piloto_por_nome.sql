-- Pesquisa piloto 

SELECT DISTINCT  concat(d.forename, ' ', d.surname) nome_completo, d.dob, d.nationality 
	FROM driver d 
	JOIN results r 
		ON d.driverid = r.driverid 
	WHERE r.constructorid = 6
		AND d.forename = 'Michael'