from database import Db
from pydantic import BaseModel

class Escuderia(BaseModel):
    consctructor_ref:str
    name:str
    nationality:str
    url:str

def cria_escurderia(ref, nome, nacio, url):
    """Escreve escuderia na base

    Args:
        escuderia (Escuderia): Nome do usuario

    Returns:
        Bool: Se inserir corretamente retorna True
    """

    db = Db()

    cursor = db.conn.cursor()
    # TODO alterar a tabela de escuderia, mudar o id pra serial.
    query_get_max_id = "SELECT MAX(constructorid) FROM constructors"
    max_id = int(cursor.execute(query_get_max_id).fetchone()[0])
    query = (
        "INSERT INTO constructors"
        "   VALUES (?,?,?,?,?)"
    )

    row = cursor.execute(query, max_id+1, ref, nome, nacio, url)
    db.conn.commit()

    return True

cria_escurderia( 'felipe', 'Felipe', 'Brazil', 'www.felipe.com' )
