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


    def select_and_convert_to_json(self, query, *params):
        cursor = self.conn.cursor()
        
        results = []
        cursor.execute(query, params)
        for row in cursor:
            results.append(row_to_json(row, cursor))

        return results


def row_to_json(row, cursor):
    dicionario = {}
    columns = [column[0] for column in cursor.description]

    for value, header in zip(row, columns):
        dicionario[header] = value

    return json.dumps(dicionario)
