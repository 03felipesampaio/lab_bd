CREATE TYPE userType AS ENUM ('Administrador', 'Escuderia', 'Piloto');

-- Tabela de usuarios
CREATE TABLE users(
	userid SERIAL PRIMARY KEY,
	login TEXT,
	password TEXT,
	tipo userType,
	idoriginal_constructor int REFERENCES constructors(constructorid) ON DELETE CASCADE,
	idoriginal_driver int REFERENCES driver(driverid) ON DELETE CASCADE,
	CONSTRAINT fk_user_driver_or_constructor
		CHECK (
			-- Verifica se usuario eh piloto
			(idoriginal_constructor IS NULL 
			  AND idoriginal_driver IS NOT NULL )
			-- Verifica se usuario eh escuderia
			OR (idoriginal_constructor IS NOT NULL 
			  AND idoriginal_driver IS NULL) 
			-- Verifica se usuario eh admin
			OR (idoriginal_constructor IS NULL 
			  AND idoriginal_driver IS NULL)
		)
);


-- Adiciona user de piloto ao cria-lo
CREATE OR REPLACE FUNCTION add_driver_user()
   RETURNS TRIGGER
AS $$
BEGIN
   IF EXISTS (SELECT * FROM users WHERE tipo = 'Piloto' AND UPPER(login) = UPPER(NEW.driverref || '_d'))
   	THEN
   		RAISE EXCEPTION 'Piloto Duplicado';
	ELSE
		INSERT INTO users(login, password, tipo, idoriginal_driver)
			VALUES(NEW.driverref || '_d', MD5(NEW.driverref), 'Piloto', NEW.driverid);
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para criar novo usuario de piloto depois de cada insercao
CREATE TRIGGER add_driver_user
  AFTER INSERT
  ON driver
  FOR EACH ROW
  EXECUTE PROCEDURE add_driver_user();
  

-- Funcao para adicionar escuderias
CREATE OR REPLACE FUNCTION add_constructors_user()
   RETURNS TRIGGER
AS $$
BEGIN
   IF EXISTS (SELECT * FROM users
			  WHERE tipo = 'Escuderia' AND UPPER(login) = UPPER(NEW.constructorref || '_c'))
   	THEN
   		RAISE EXCEPTION 'Escuderia Duplicada';
	ELSE
		INSERT INTO users(login, password, tipo, idoriginal_constructor)
			VALUES(NEW.constructorref || '_c', MD5(NEW.constructorref), 'Escuderia', NEW.constructorid);
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para criar novo usuario de escuderia depois de cada insercao
CREATE TRIGGER add_constructors_user
  AFTER INSERT
  ON constructors
  FOR EACH ROW
  EXECUTE PROCEDURE add_constructors_user();


-- Insere usuario ADMIN na lista de usuarios
INSERT INTO users(login, password, tipo) VALUES ('admin', MD5('admin'), 'Administrador');

-- Insere as escuderias ja existentes na tabela de usuarios
INSERT INTO users(login, password, tipo, idoriginal_constructor)
SELECT
  constructorref || '_c' AS login,
  MD5(constructorref) AS password,
  'Escuderia' AS tipo,
  constructorid
	FROM constructors;

-- Insere os pilotos ja existentes na tabela de usuarios
INSERT INTO users(login,password,tipo,idoriginal_driver)
SELECT
  driverref || '_d' AS login,
  MD5(driverref) AS password,
  'Piloto' AS tipo,
  driverid
	FROM driver;


-- Cria tabela de logs, que sera atualizada pela funcao login
CREATE TABLE log_table(
	logid BIGSERIAL PRIMARY KEY,
	userid INT,
	acess TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	CONSTRAINT fk_log_user FOREIGN KEY(userid) REFERENCES users(userid) ON DELETE CASCADE
)