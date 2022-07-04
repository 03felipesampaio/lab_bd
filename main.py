from login import Login, connect
from admin import admin_overview, admin_relatorios
from escuderia import Escuderia, cria_escuderia, escuderia_overview, escuderia_relatorios
from piloto import Piloto, cria_piloto, piloto_overview, piloto_relatorios


from fastapi import FastAPI
from typing import Union
from enum import Enum

class TiposUsuario(str, Enum):
    admin = "Administrador"
    escuderia = "Escuderia"
    piloto = "Piloto"


app = FastAPI()

usuario:Union[dict,None] = None

@app.post("/api/login")
def try_login(login:Login):
    usuario = connect(login.user, login.password)
    return usuario


@app.get("/api")
def get_overview(tipo:TiposUsuario):
    if tipo.value == 'Administrador':
        return admin_overview()
    elif tipo.value == 'Escuderia':
        return escuderia_overview(10)
    elif tipo.value == 'Piloto':
        return piloto_overview(856)


@app.get("/api/relatorios")
def get_relatorios(tipo:TiposUsuario):
    if tipo.value == 'Administrador':
        return admin_relatorios()
    elif tipo.value == 'Escuderia':
        return escuderia_relatorios(6)
    elif tipo.value == 'Piloto':
        return piloto_relatorios(30)


@app.post("/api/escuderias")
def post_escuderia(esc:Escuderia):
    return cria_escuderia(esc.constructor_ref, esc.name, esc.nationality, esc.url)


@app.get("/api/escuderias/{escuderia}/pilotos")
def get_piloto_por_nome(escuderia:str, nome:str):
    pass


@app.post("/api/pilotos")
def post_piloto(pil:Piloto):
        return cria_piloto(
            pil.driver_ref, pil.number, pil.code,
            pil.forename, pil.surname, pil.date_of_birth,
            pil.nationality)
    