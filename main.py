from login import Login, User, connect
from admin import admin_overview, admin_relatorios, aeroportos_proximos
from escuderia import Escuderia, cria_escuderia, escuderia_overview, escuderia_relatorios
from piloto import Piloto, cria_piloto, piloto_overview, piloto_relatorios, procura_piloto_por_nome


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from enum import Enum

class TiposUsuario(str, Enum):
    admin = "Administrador"
    escuderia = "Escuderia"
    piloto = "Piloto"


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/login")
def try_login(login:Login):
    return connect(login.user, login.password)


@app.post("/api/overview")
def get_overview(user:User):
    if user.tipo == 'Administrador':
        return admin_overview()
    elif user.tipo == 'Escuderia':
        return escuderia_overview(user.id_constructor)
    elif user.tipo == 'Piloto':
        return piloto_overview(user.id_driver)


@app.post("/api/relatorios")
def get_relatorios(user:User):
    if user.tipo == 'Administrador':
        return admin_relatorios()
    elif user.tipo == 'Escuderia':
        return escuderia_relatorios(user.id_constructor)
    elif user.tipo == 'Piloto':
        return piloto_relatorios(user.id_driver)


@app.post("/api/relatorios/{cidade}")
def get_relatorio_2(user:User, cidade:str):
    if user.tipo == 'Adminstrador':
        return aeroportos_proximos(cidade)


@app.post("/api/escuderias")
def post_escuderia(user:User, esc:Escuderia):
    return cria_escuderia(esc.constructor_ref, esc.name, esc.nationality, esc.url)


@app.post("/api/escuderias/{escuderia}/pilotos")
def get_piloto_por_nome(user:User, nome:str):
    if user.tipo == 'Escuderia':
        return procura_piloto_por_nome(user.id_constructor, nome)


@app.post("/api/pilotos")
def post_piloto(user:User, pil:Piloto):
        if user.tipo == "Administrador":
            return cria_piloto(
                pil.driver_ref, pil.number, pil.code,
                pil.forename, pil.surname, pil.date_of_birth,
                pil.nationality)
        else:
            raise ValueError('Usuario invalido')
    