import pyodbc
import json

# TODO Add documentacao https://www.sqlshack.com/configure-odbc-drivers-for-postgresql/

class Db:
    def __init__(self) -> None:
        conn_str = (
            "DRIVER={PostgreSQL Unicode};"
            "DATABASE=proj_final;"
            "UID=postgres;"
            "PWD=1;"
            "SERVER=localhost;"
            "PORT=5432;"
        )
        self.conn = pyodbc.connect(conn_str)


    # def select(self, query, *params)

def row_to_json(cursor, row):
    dicionario = {}
    columns = [column[0] for column in cursor.description]

    for value, header in zip(row, columns):
        dicionario[header] = value

    return json.dumps(dicionario)
