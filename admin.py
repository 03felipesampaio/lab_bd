from database import Db

def admin_overview():
    db = Db()
    
    query_qtd_pilotos = "SELECT COUNT(*) qtd_pilotos FROM driver"
    query_qtd_escuderias = "SELECT COUNT(*) qtd_escuderias FROM constructors"
    query_qtd_corridas = "SELECT COUNT(*) qtd_corridas FROM races"
    query_qtd_temporadas = "SELECT COUNT(*) qtd_temporadas FROM seasons"

    results = {
        'qtd_pilotos'    : db.select_and_convert_to_json(query_qtd_pilotos),
        'qtd_escuderias' : db.select_and_convert_to_json(query_qtd_escuderias),
        'qtd_corridas'   : db.select_and_convert_to_json(query_qtd_corridas),
        'qtd_temporadas' : db.select_and_convert_to_json(query_qtd_temporadas)
    }

    return results