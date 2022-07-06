from database import Db

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

    query_login = (
        "SELECT userid, tipo, idoriginal_constructor, idoriginal_driver FROM users"
        "   WHERE login = ? AND password = MD5(?)"
    )
    
    usuario = db.select_and_convert_to_json(query_login, user, password)

    if usuario:
        query_insert_log = (
            "INSERT INTO log_table (userid, acess)"
	        "   VALUES (?, now())"
        )

        # Insere login na tabela de logs
        cursor = db.conn.cursor()
        cursor.execute(query_insert_log, usuario[0]['userid'])
        db.conn.commit()
        return usuario
    else:
        raise ValueError('User ou senha invalidos')


def get_name(user: User):
    db = Db()

    cursor = db.conn.cursor()

    query1 = (
        "SELECT (forename || ' ' || surname) as name from driver where driverid = ?"
    )
    query2 = (
        "SELECT name from constructors where constructorid = ?"
    )
    
    if(user.tipo == "Administrador"):
        d = dict()
        d['name'] = "Administrador"
        return d
    elif(user.tipo == "Piloto"):
        usuario = db.select_and_convert_to_json(query1, user.id_driver)
    else:
        usuario = db.select_and_convert_to_json(query2, user.id_constructor)

    if usuario:
        return usuario.pop()


# def get_usuario(id):
#     db = Db()

#     query = (
#         "SELECT userid, tipo, idoriginal_constructor, idoriginal_driver FROM users"
#         "   WHERE userid = ?"
#     )

#     db.select_and_convert_to_json()

