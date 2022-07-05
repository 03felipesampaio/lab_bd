from database import Db, row_to_json

from pydantic import BaseModel


class Login(BaseModel):
    user:str
    password:str


class User(BaseModel):
    user_id:int
    tipo:str
    id_constructor:int = None
    id_driver:int = None


def connect(user, password) -> User:
    """Procura um match de usuario e senha e retorna
    informacoes do usuario

    Args:
        user (str): Nome do usuario
        password (str): Senha

    Raises:
        ValueError: Caso o usuario ou senha estejam errados

    Returns:
        User: Informacoes do usuario
    """

    db = Db()

    cursor = db.conn.cursor()

    query = (
        "SELECT userid, tipo, idoriginal_constructor, idoriginal_driver FROM users"
        "   WHERE login = ? AND password = MD5(?)"
    )
    
    usuario = db.select_and_convert_to_json(query, user, password)

    if usuario:            
        return usuario
    else:
        raise ValueError('User ou senha invalidos')


# def get_usuario(id):
#     db = Db()

#     query = (
#         "SELECT userid, tipo, idoriginal_constructor, idoriginal_driver FROM users"
#         "   WHERE userid = ?"
#     )

#     db.select_and_convert_to_json()

