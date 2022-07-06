import pyodbc
from dotenv import dotenv_values

config = dotenv_values(".env")

# TODO Add documentacao https://www.sqlshack.com/configure-odbc-drivers-for-postgresql/

class Db:
    """Classe para acessar a base de dados
    """

    def __init__(self) -> None:
        conn_str = (
            "DRIVER={PostgreSQL Unicode};"
            f"DATABASE={config['DATABASE']};"
            f"UID={config['USUARIO']};"
            f"PWD={config['SENHA']};"
            "SERVER=localhost;"
            "PORT=5432;"
        )
        self.conn = pyodbc.connect(conn_str)


    def select_and_convert_to_json(self, query, *params):
        """Operacao de select na base e retorna os resultados
        em um formato ideal para APIs

        Args:
            query (str): Query a ser executada

        Returns:
            JSON: JSON com resultados
        """

        cursor = self.conn.cursor()
        
        results = []
        cursor.execute(query, params)
        for row in cursor:
            results.append(row_to_json(row, cursor))

        return results


def row_to_json(row, cursor):
    """Os resultados das queries vem sem cabecalho
    e em formato de tuplas Ex.: (Lab', 'de'), ('Base', 'Dados').
    Precisamos adicionar cabecalho e alterar para JSON para
    utilizar na API

    Args:
        row (tuple): Linha do resultado
        cursor (cursor): Cursor da query

    Returns:
       JSON: Tupla em JSON com cabecalho
    """
    dicionario = {}
    # Pega os cabecalhos
    columns = [column[0] for column in cursor.description]

    # Itera sobre a linha e cabecalho ao mesmo tempo
    for value, header in zip(row, columns):
        # Adiciona ao dicionario
        dicionario[header] = value

    return dicionario
