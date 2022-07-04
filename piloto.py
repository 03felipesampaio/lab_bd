from database import Db, row_to_json
from pydantic import BaseModel
from datetime import date

class Piloto(BaseModel):
    driver_ref:str
    number:str
    code:str
    forename:str
    surname:str
    date_of_birth:date
    nationality:str


def cria_piloto(ref, num, cod, nome, sobrenome, nasc, nacio):
    """Escreve piloto na base

    Args:
        piloto (piloto): Nome do usuario

    Returns:
        JSON: Se inserir corretamente retorna a linha inserida
    """

    db = Db()

    cursor = db.conn.cursor()
    # TODO alterar a tabela de piloto, mudar o id pra serial.
    query_get_max_id = "SELECT MAX(driverid) FROM driver"
    max_id = int(cursor.execute(query_get_max_id).fetchone()[0])
    query = (
        "INSERT INTO driver"
        "   VALUES (?,?,?,?,?,?,?,?)"
        "   RETURNING *"
    )

    row = cursor.execute(query, max_id+1, ref,
            num, cod, nome, sobrenome, nasc, nacio
        ).fetchone()
    db.conn.commit()

    return row_to_json(row, cursor)


# def procura_piloto_por_nome(id_escuderia:int, id_piloto:int):
#     query = (
#         "SELECT * FROM"
#     )


def check_piloto(id_piloto:int):
    db = Db()
    cursor = db.conn.cursor()
    cursor.execute("SELECT driverid FROM driver WHERE driverid = ?", id_piloto)
    if cursor.fetchone(): return True
    else: return False


def piloto_overview(id_piloto:int):
    
    if not check_piloto(id_piloto):
        raise ValueError('Piloto nao existe')
    
    db = Db()

    # Queries referentes as mesmas do arquivo ./queries/overviewConstructor.sql
    query_qtd_vitorias = "SELECT COUNT(*) qtd_vitorias " \
        "FROM results WHERE position = 1 AND driverid = ?"

    query_prim_e_ult_ano = (
        "SELECT MIN(RA.year) prim_ano, MAX(RA.year) ult_ano "
            "FROM results JOIN races RA USING (raceid) "
            "WHERE driverid = ?"
    )

    results = {
        'prim_e_ult_ano' : db.select_and_convert_to_json(query_prim_e_ult_ano, id_piloto),
        'qtd_vitorias'   : db.select_and_convert_to_json(query_qtd_vitorias, id_piloto),
    }

    return results


def piloto_relatorios(id_piloto:int):
    if not check_piloto(id_piloto):
        raise ValueError('piloto nao existe')
    
    db = Db()

    # Queries referentes as mesmas do arquivo ./queries/overviewConstructor.sql
    # TODO Criar indice

    # query_index_relatorio_5 = (
    #     "CREATE INDEX IF NOT EXISTS wins_construc " 
    #     "   ON results(driverid, constructorid) WHERE position = 1;"
    #     "-- DROP INDEX wins_construc;"
    # )

    query_relatorio_5 = (
        "SELECT RA.name nome, CAST(RA.YEAR AS VARCHAR(4)) ano, COUNT(*) vitorias"
        "    FROM results R"
        "    JOIN races RA USING(raceid)"
        "    WHERE R.position = 1 AND R.driverid = ?"
        "    GROUP BY ROLLUP(RA.year, RA.name)"
        "    ORDER BY RA.year DESC, count(*)  DESC;"
    )

    query_relatorio_6 = (
        "SELECT S.status, COUNT(*) Resultados from results R"
        "    JOIN status S USING(statusid)"
        "    WHERE R.driverid = ?"
        "    GROUP BY S.statusid"
        "    ORDER BY S.status;"
    )


    # cursor = db.conn.cursor()
    # cursor.execute(query_index_relatorio_5)

    results = {
        'relatorio_5' : db.select_and_convert_to_json(query_relatorio_5, id_piloto),
        'relatorio_6' : db.select_and_convert_to_json(query_relatorio_6, id_piloto)
    }

    return results
