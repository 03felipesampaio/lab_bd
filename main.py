# Libs para API
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Funcoes de login
from login import Login, User, connect, get_name
# Funcoes do admin
from admin import admin_overview, admin_relatorio_1, aeroportos_proximos
# Funcoes da escuderia
from escuderia import Escuderia, cria_escuderia, escuderia_overview, escuderia_relatorios
# Funcoes do piloto
from piloto import Piloto, cria_piloto, piloto_overview, piloto_relatorios, procura_piloto_por_nome


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
    usuario = connect(login.user, login.password)
    if usuario:
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuario ou senha incorretos")

@app.post("/api/name")
def name(user:User):
    return get_name(user)


@app.post("/api/overview")
def get_overview(user:User):
    if user.tipo == 'Administrador':
        return admin_overview()
    elif user.tipo == 'Escuderia':
        try:
            return escuderia_overview(user.id_constructor)
        except Exception as e:
            raise HTTPException(404, "Codigo da escuderia invalido")
    elif user.tipo == 'Piloto':
        try:
            return piloto_overview(user.id_driver)
        except Exception as e:
            raise HTTPException(404, "Codigo do piloto invalido")


@app.post("/api/relatorios")
def get_relatorios(user:User):
    if user.tipo == 'Administrador':
        return admin_relatorio_1()
    elif user.tipo == 'Escuderia':
        try:
            return escuderia_relatorios(user.id_constructor)
        except Exception as e:
            raise HTTPException(404, "Codigo da escuderia invalido")
    elif user.tipo == 'Piloto':
        try:
            return piloto_relatorios(user.id_driver)
        except Exception as e:
            raise HTTPException(404, "Codigo do piloto invalido")


@app.post("/api/relatorios/{cidade}")
def get_relatorio_2(user:User, cidade:str):
    if user.tipo == 'Administrador':
        return aeroportos_proximos(cidade)


@app.post("/api/escuderias")
def post_escuderia(user:User, esc:Escuderia):
    if user.tipo == 'Administrador':
        return cria_escuderia(esc.constructor_ref, esc.name, esc.nationality, esc.url)
    else:
        raise HTTPException(404, "Usuario nao eh admin")


@app.post("/api/escuderias/{escuderia}/pilotos")
def get_piloto_por_nome(user:User, nome:str):
    if user.tipo == 'Escuderia':
        return procura_piloto_por_nome(user.id_constructor, nome)
    else:
        raise HTTPException(404, "Usuario nao eh Escuderia")


@app.post("/api/pilotos")
def post_piloto(user:User, pil:Piloto):
        if user.tipo == "Administrador":
            return cria_piloto(
                pil.driver_ref, pil.number, pil.code,
                pil.forename, pil.surname, pil.date_of_birth,
                pil.nationality)
        else:
            raise HTTPException(404, "Usuario nao e administrador")
    