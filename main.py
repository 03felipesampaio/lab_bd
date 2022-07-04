from login import Login, User, connect
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


@app.post("/api/login")
def try_login(login:Login):
    return connect(login.user, login.password)


@app.get("/api")
def get_overview(user:User):
    if user.tipo == 'Administrador':
        return admin_overview()
    elif user.tipo == 'Escuderia':
        return escuderia_overview(user.id_construtor)
    elif user.tipo == 'Piloto':
        return piloto_overview(user.id_driver)


@app.get("/api/relatorios")
def get_relatorios(user:User):
    if user.tipo == 'Administrador':
        return admin_relatorios()
    elif user.tipo == 'Escuderia':
        return escuderia_relatorios(user.id_construtor)
    elif user.tipo == 'Piloto':
        return piloto_relatorios(user.id_driver)


@app.post("/api/escuderias")
def post_escuderia(user:User, esc:Escuderia):
    return cria_escuderia(esc.constructor_ref, esc.name, esc.nationality, esc.url)


@app.get("/api/escuderias/{escuderia}/pilotos")
def get_piloto_por_nome(escuderia:str, nome:str):
    pass


@app.post("/api/pilotos")
def post_piloto(user:User, pil:Piloto):
        if user.tipo == "Administrador":
            return cria_piloto(
                pil.driver_ref, pil.number, pil.code,
                pil.forename, pil.surname, pil.date_of_birth,
                pil.nationality)
        else:
            raise ValueError('Usuario invalido')
    