from fastapi import FastAPI
from typing import Union

from models import Login, Escuderia, Piloto

from login import connect

app = FastAPI()


user = {
    'role' : 'admin',
    'user' : 'admin',
    'password' : 'admin1'
}


@app.post("/api/login")
def try_login(login:Login):
    return connect(login.user, login.password)


@app.get("/api/admin")
def get_overview_admin():
    pass


@app.post("/api/escuderias")
def cria_escuderia(escuderia:Escuderia):
    return escuderia


@app.get("/api/escuderias/{escuderia}/pilotos")
def get_piloto_por_nome(escuderia:str, nome:str):
    pass


@app.get("/api/escuderias/{escuderia}")
def get_overview_escuderia(escuderia):
    pass


@app.get("/api/pilotos/{id_piloto}")
def get_overview_piloto(id_piloto):
    pass


@app.post("/api/pilotos")
def cria_piloto(piloto:Piloto):
    return piloto

    