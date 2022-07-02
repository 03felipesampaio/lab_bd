CREATE EXTENSION IF NOT EXISTS Cube;
CREATE EXTENSION IF NOT EXISTS EarthDistance;

CREATE INDEX city_br ON geocities15K(country, name, lat, long);
-- DROP INDEX city_br;

CREATE INDEX air_br ON airports(isocountry, type) INCLUDE(
iatacode, name, latdeg, longdeg, city, type);
-- DROP INDEX air_br;

CREATE OR REPLACE VIEW cidades_brasileiras AS 
	SELECT G."name", G.lat, G.long
	FROM geocities15k G
	WHERE G.country='BR';
-- Drop view cidades_brasileiras;
	
CREATE OR REPLACE VIEW aeroportos_brasileiros AS 
	SELECT A.iatacode, A."name" "Aeroporto", A.latdeg "Latitude", A.longdeg "Longitude",
		A.city "Cid_Aero", A."type"
	FROM airports A
	WHERE A.isocountry='BR' AND (A."type"='medium_airport' OR A."type"='large_airport');
-- Drop view aeroportos_brasileiros;
	
SELECT C.Name "Cidade", A.iatacode, A."Aeroporto", A."Cid_Aero",
		earth_distance(ll_to_earth(A."Latitude", A."Longitude"
		) , ll_to_earth(C.Lat, C.Long)) "Distância", A."type"
	FROM aeroportos_brasileiros A, cidades_brasileiras C
	WHERE earth_distance(ll_to_earth(A."Latitude", A."Longitude"
) , ll_to_earth(C.Lat, C.Long)) <= 100000 AND C."name"='Barra Bonita';