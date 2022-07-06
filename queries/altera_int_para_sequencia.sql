-- Altera o campo driverid da tabela driver para iterar a cada insercao
CREATE SEQUENCE seq_id_driver MINVALUE 856;
ALTER TABLE driver ALTER driverid SET DEFAULT nextval('seq_id_driver');
ALTER SEQUENCE seq_id_driver OWNED BY driver.driverid;

-- Altera o campo constructorid da tabela constructors para iterar a cada insercao
CREATE SEQUENCE seq_id_constructor MINVALUE 216;
ALTER TABLE constructors ALTER constructorid SET DEFAULT nextval('seq_id_constructor');
ALTER SEQUENCE seq_id_constructor OWNED BY constructors.constructorid;