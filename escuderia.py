from database import Db, row_to_json
from pydantic import BaseModel

class Escuderia(BaseModel):
    constructor_ref:str
    name:str
    nationality:str
    url:str

def cria_escuderia(ref, nome, nacio, url):
    """Escreve escuderia na base

    Args:
        escuderia (Escuderia): Nome do usuario

    Returns:
        JSON: Se inserir corretamente retorna a linha inserida 
    """

    db = Db()

    cursor = db.conn.cursor()
    # TODO alterar a tabela de escuderia, mudar o id pra serial.
    query_get_max_id = "SELECT MAX(constructorid) FROM constructors"
    max_id = int(cursor.execute(query_get_max_id).fetchone()[0])
    query = (
        "INSERT INTO constructors"
        "   VALUES (?,?,?,?,?)"
        "   RETURNING *"
    )

    row = cursor.execute(query, max_id+1, ref, nome, nacio, url).fetchone()
    db.conn.commit()

    return row_to_json(row, cursor)


def check_escuderia(id_escuderia:int):
    """Verifica se escuderia ja existe

    Args:
        id_escuderia (int): _description_

    Returns:
        _type_: _description_
    """
    
    db = Db()
    cursor = db.conn.cursor()
    # Verifica se existe uma escuderia com esse id
    cursor.execute("SELECT constructorid FROM constructors WHERE constructorid = ?", id_escuderia)
    if cursor.fetchone(): return True
    else: return False


def escuderia_overview(id_escuderia:int):
    if not check_escuderia(id_escuderia):
        raise ValueError('Escuderia nao existe')
    
    db = Db()

    # Queries referente ao arquivo ./queries/overviewConstructor.sql
    query_qtd_vitorias = "SELECT COUNT(*) qtd_vitorias FROM results " \
        "WHERE position = 1 AND constructorid = ?;"

    query_qtd_pilotos = "SELECT COUNT(DISTINCT(driverid)) qtd_pilotos " \
        "FROM results " \
        "WHERE constructorid = ?;"

    query_prim_e_ult_ano = (
        "SELECT MIN(RA.year) prim_ano, MAX(RA.year) ult_ano" \
        "   FROM results " \
        "   JOIN races RA USING (raceid) "\
        "   WHERE constructorid = ?;"
    )

    results = {
        'firstAndLastYearsOfData' : db.select_and_convert_to_json(query_prim_e_ult_ano, id_escuderia),
        'numberOfWins'   : db.select_and_convert_to_json(query_qtd_vitorias, id_escuderia),
        'numberOfPilots'    : db.select_and_convert_to_json(query_qtd_pilotos, id_escuderia)
    }

    return results


def escuderia_relatorios(id_escuderia:int):
    if not check_escuderia(id_escuderia):
        raise ValueError('Escuderia nao existe')
    
    db = Db()

    # Queries referentes as mesmas do arquivo ./queries/overviewConstructor.sql
    query_index_relatorio_3 = (
        "CREATE INDEX IF NOT EXISTS wins_construc " 
        "   ON results(driverid, constructorid) WHERE position = 1;"
        "-- DROP INDEX wins_construc;"
    )

    query_relatorio_3 = (
        "SELECT D.forename Nome, D.surname Sobrenome, COUNT(*) vitorias"
        "   FROM results R"
        "       JOIN driver D USING (driverid)"
        "       WHERE R.position = 1 AND R.constructorid = ?"
        "       GROUP BY D.driverid"
        "       ORDER BY COUNT(*) DESC;"
    )

    query_relatorio_4 = (
        "SELECT S.status, COUNT(*) Resultados from results R"
        "    JOIN status S USING(statusid)"
        "    WHERE R.constructorid = ?"
        "    GROUP BY S.statusid"
        "    ORDER BY COUNT(*) DESC;"
    )


    cursor = db.conn.cursor()
    cursor.execute(query_index_relatorio_3)

    results = {
        'relatorio_3' : db.select_and_convert_to_json(query_relatorio_3, id_escuderia),
        'relatorio_4' : db.select_and_convert_to_json(query_relatorio_4, id_escuderia)
    }

    return results