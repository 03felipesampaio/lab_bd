from fastapi import FastAPI
from typing import Union


from login import Login, connect
from piloto import Piloto
from escuderia import Escuderia, cria_escurderia

app = FastAPI()

usuario = None

@app.post("/api/login")
def try_login(login:Login):
    usuario = connect(login.user, login.password)
    return usuario


@app.get("/api/admin")
def get_overview_admin():
    pass


@app.post("/api/escuderias")
def post_escuderia(esc:Escuderia):
    return cria_escurderia(esc.consctructor_ref, esc.name, esc.url)


@app.get("/api/escuderias/{escuderia}/pilotos")
def get_piloto_por_nome(escuderia:str, nome:str):
    return cria_piloto()


@app.get("/api/escuderias/{escuderia}")
def get_overview_escuderia(escuderia):
    pass


@app.get("/api/pilotos/{id_piloto}")
def get_overview_piloto(id_piloto):
    pass


@app.post("/api/pilotos")
def cria_piloto(piloto:Piloto):
    return piloto

    