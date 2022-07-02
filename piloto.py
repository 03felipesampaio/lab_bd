from database import Db
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
    """Escreve escuderia na base

    Args:
        escuderia (Escuderia): Nome do usuario

    Returns:
        Bool: Se inserir corretamente retorna True
    """

    db = Db()

    cursor = db.conn.cursor()
    # TODO alterar a tabela de escuderia, mudar o id pra serial.
    query_get_max_id = "SELECT MAX(driverid) FROM driver"
    max_id = int(cursor.execute(query_get_max_id).fetchone()[0])
    query = (
        "INSERT INTO constructors"
        "   VALUES (?,?,?,?,?)"
    )

    row = cursor.execute(query, max_id+1, ref, na, nationality, url)
    db.conn.commit()

    return True