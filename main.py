from fastapi import FastAPI
from typing import Union


from login import Login, connect
from piloto import Piloto, cria_piloto, piloto_overview
from escuderia import Escuderia, cria_escuderia, escuderia_overview

app = FastAPI()

usuario:Union[dict,None] = None

@app.post("/api/login")
def try_login(login:Login):
    usuario = connect(login.user, login.password)
    return usuario


@app.get("/api")
def get_overview():
    if usuario.tipo == 'Administrador':
        pass
    elif usuario.tipo == 'Escuderia':
        escuderia_overview(usuario.idoriginal_constructor)
    elif usuario.tipo == 'Piloto':
        piloto_overview(usuario.idoriginal_driver)


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
    