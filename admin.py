from database import Db

def admin_overview():
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

def admin_relatorios():
    db = Db()
    
    query_qtd_resultados = (
        "SELECT S.status, COUNT(*) Resultados from results R"
	        "JOIN status S USING(statusid)"
	        "GROUP BY S.statusid"
	        "ORDER BY S.status;"
    )
    

    results = {
        'relatorio_1' : db.select_and_convert_to_json(query_qtd_resultados)
    }

    return results


def aeroportos_proximos(cidade:str):
    pass