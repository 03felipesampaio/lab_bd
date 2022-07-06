CREATE OR REPLACE PROCEDURE prepara_relatorio_2()
LANGUAGE plpgsql
AS $$
DECLARE
-- variable declaration
BEGIN
	CREATE EXTENSION IF NOT EXISTS Cube;
	CREATE EXTENSION IF NOT EXISTS EarthDistance;
	
	CREATE INDEX IF NOT EXISTS city_br ON geocities15K(country, name, lat, long);
	-- DROP INDEX city_br;
	
	CREATE INDEX IF NOT EXISTS air_br ON airports(isocountry, type) INCLUDE(
	iatacode, name, latdeg, longdeg, city, type);
	-- DROP INDEX air_br;
	
	CREATE OR REPLACE VIEW cidades_brasileiras AS 
		SELECT G.name, G.lat, G.long
		FROM geocities15k G
		WHERE G.country='BR';
	-- Drop view cidades_brasileiras;
		
	CREATE OR REPLACE VIEW aeroportos_brasileiros AS 
		SELECT A.iatacode, A.name aeroporto, A.latdeg latitude, A.longdeg longitude,
			A.city cid_aero, A.type
		FROM airports A
		WHERE A.isocountry='BR' AND (A.type='medium_airport' OR A.type='large_airport');
	-- DROP VIEW aeroportos_brasileiros
END; $$