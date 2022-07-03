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


def piloto_overview(id_piloto:int):
    
    if not check_piloto(id_piloto):
        raise ValueError('Piloto nao existe')
    
    db = Db()

    # Queries referentes as mesmas do arquivo ./queries/overviewConstructor.sql
    querie_qtd_vitorias = "SELECT COUNT(*) qtd_vitorias " \
        "FROM results WHERE position = 1 AND driverid = ?"

    querie_prim_e_ult_ano = (
        "SELECT MIN(RA.year) prim_ano, MAX(RA.year) ult_ano "
            "FROM results JOIN races RA USING (raceid) "
            "WHERE driverid = ?"
    )

    results = {
        'prim_e_ult_ano' : db.select_and_convert_to_json(querie_prim_e_ult_ano, id_piloto),
        'qtd_vitorias'   : db.select_and_convert_to_json(querie_qtd_vitorias, id_piloto),
    }

    return results


def check_piloto(id_piloto:int):
    db = Db()
    cursor = db.conn.cursor()
    cursor.execute("SELECT driverid FROM driver WHERE driverid = ?", id_piloto)
    if cursor.fetchone(): return True
    else: return False
