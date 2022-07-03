from database import Db
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

    row = db.select_and_convert_to_json(query, max_id+1, ref, nome, nacio, url)
    db.conn.commit()

    return row


def escuderia_overview(id_escuderia):
    db = Db()

    # Queries referentes as mesmas do arquivo ./queries/overviewConstructor.sql
    querie_qtd_vitorias = "SELECT COUNT(*) FROM results " \
        "WHERE position = 1 AND constructorid = ?;"

    querie_qtd_pilotos = "SELECT COUNT(DISTINCT(driverid)) FROM results " \
        "WHERE constructorid = ?;"

    querie_prim_e_ult_ano = (
        "SELECT MIN(RA.year), MAX(RA.year) " \
        "   FROM results " \
        "   JOIN races RA USING (raceid) "\
        "   WHERE constructorid = ?;"
    )

    results = {
        'prim_e_ult_ano' : db.select_and_convert_to_json(querie_prim_e_ult_ano, id_escuderia),
        'qtd_vitorias'   : db.select_and_convert_to_json(querie_qtd_vitorias, id_escuderia),
        'qtd_pilotos'    : db.select_and_convert_to_json(querie_qtd_pilotos, id_escuderia)
    }

    return results
