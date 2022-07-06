-- O setup dessa query, incluindo os indices estao no arquivo setup_R2.sql
SELECT C.Name Cidade, A.iatacode, a.aeroporto, A.cid_aero,
		earth_distance(
			ll_to_earth(
				A.latitude, A.longitude
			), 
			ll_to_earth(
				C.Lat, C.Long
			)
		) distancia, A.type
	FROM aeroportos_brasileiros A, cidades_brasileiras C
	WHERE 
		earth_distance(
			ll_to_earth(
				A.latitude, A.longitude
			) , 
			ll_to_earth(
				C.lat, C.long
			)
		) <= 100000 AND C.name='Campinas';
