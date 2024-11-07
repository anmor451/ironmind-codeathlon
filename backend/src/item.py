from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float

class Sexe(BaseModel):
    sexePersonne: str

class Programme(BaseModel):
    nomProgramme: str

class Inscription(BaseModel):
    fname: str
    lname: str
    email: str
    passwd: str
    sexe: str

class Events(BaseModel):
    date: str # Je sais que c'est sensé être Datetime, mais le module ne fonctionne pas alors flemme
    name: str