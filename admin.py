from database import Db

def admin_overview():
    """Retorna overview do administrador

    Returns:
        JSON: Cada query sera retornada como um JSON
    """
    db = Db()
    
    query_qtd_pilotos = "SELECT COUNT(*) qtd_pilotos FROM driver"
    query_qtd_escuderias = "SELECT COUNT(*) qtd_escuderias FROM constructors"
    query_qtd_corridas = "SELECT COUNT(*) qtd_corridas FROM races"
    query_qtd_temporadas = "SELECT COUNT(*) qtd_temporadas FROM seasons"

    results = {
        'numberOfPilots'  : db.select_and_convert_to_json(query_qtd_pilotos),
        'numberOfTeams'   : db.select_and_convert_to_json(query_qtd_escuderias),
        'numberOfRaces'   : db.select_and_convert_to_json(query_qtd_corridas),
        'numberOfSeasons' : db.select_and_convert_to_json(query_qtd_temporadas)
    }

    return results

def admin_relatorio_1():
    """Devolve o primeiro relatorio do administrador

    Returns:
        JSON: Json com relatorio
    """
    db = Db()
    
    query_qtd_resultados = (
        "SELECT S.status, COUNT(*) Resultados from results R "
	        " JOIN status S USING(statusid)"
	        " GROUP BY S.statusid"
	        " ORDER BY S.status;"
    )

    results = {
        'relatorio_1' : db.select_and_convert_to_json(query_qtd_resultados)
    }

    return results


def aeroportos_proximos(cidade:str):
    """Retorna o relatorio dois do administrador. A partir de uma
    cidade, procura os aeroportos no raio de 100km

    Args:
        cidade (str): Nome da cidade a ser buscada

    Returns:
        JSON: JSON com os resultados
    """
    db = Db()
    
    query_aeroportos = (
        # "-- O setup dessa query, incluindo os indices estao no arquivo setup_R2.sql"
        "SELECT C.Name Cidade, A.iatacode, a.aeroporto, A.cid_aero,"
        "    earth_distance("
        "        ll_to_earth("
        "            A.latitude, A.longitude"
        "        )," 
        "        ll_to_earth("
        "            C.Lat, C.Long"
                "	)"
                ") distancia, A.type"
        "   FROM aeroportos_brasileiros A, cidades_brasileiras C"
        "   WHERE "
        "   	earth_distance("
        "   		ll_to_earth("
        "   			A.latitude, A.longitude"
        "   		) , "
        "   		ll_to_earth("
        "   			C.lat, C.long"
        "   		)"
        "   	) <= 100000 AND C.name='?';"
    )

    results = {
        'relatorio_2' : db.select_and_convert_to_json(query_aeroportos, cidade)
    }

    return results