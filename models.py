from pydantic import BaseModel


# TODO Lembrar de verificar se os tipos de dados estao corretos
class Escuderia(BaseModel):
    consctructor_ref:str
    name:str
    nationality:str
    url:str
    
class Piloto(BaseModel):
    driver_ref:str
    number:str
    code:str
    forename:str
    surname:str
    date_of_birth:str
    nationality:str