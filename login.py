from database import Db, row_to_json

def connect(user, password):
    """Procura um match de usuario e senha e retorna
    informacoes do usuario

    Args:
        user (str): Nome do usuario
        password (str): Senha

    Raises:
        ValueError: Caso o usuario ou senha estejam errados

    Returns:
        Json: Informacoes do usuario
    """

    db = Db()

    cursor = db.conn.cursor()

    query = (
        "SELECT userid, login, tipo, idoriginal_constructor idoriginal_driver FROM users"
        "   WHERE login = ? AND password = MD5(?)"
    )

    cursor.execute(query, user, password)

    row = cursor.fetchone()
    
    if row:            
        return row_to_json(cursor, row)
    else:
        raise ValueError('User ou senha invalidos')

