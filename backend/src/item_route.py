import mariadb
import hashlib
from fastapi import APIRouter, HTTPException

from src.item import Item
from src.item import Sexe
from src.item import Programme
from src.item import Inscription
from src.item import Events
from src.fonctions import verifie_age

router = APIRouter()
sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")


@router.get("/")
def index():
    return {"message": "Hello, World!"}


@router.get("/items")
def get_item():
    with sql_connection.cursor() as cursor:
        query = "SELECT name,description,price FROM items"
        cursor.execute(query)
        results = cursor.fetchall()
        return [Item(name=result[0], description=result[1], price=result[2]) for result in results]


@router.post("/item")
def add_item(item: Item):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO items (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (item.name, item.description, item.price))
        sql_connection.commit()


# Ajouter/Get le sexes des personnes
@router.post("/sexe")
def add_sexe(sexe: Sexe):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO sexe (sexe) VALUES (%s)"
        cursor.execute(sql, (sexe.sexePersonne))
        sql_connection.commit()

@router.get("/sexe")
def get_sexe():
    with sql_connection.cursor() as cursor:
        query = "SELECT sexePersonne FROM sexes"
        cursor.execute(query)
        results = cursor.fetchall()
        if results[0] not in (0,1):
            raise HTTPException(status_code=402, detail="Le sexe doit être homme ou femme")
        return [Sexe(sexePersonne=result[0]) for result in results]


# ajouter et chercher
@router.post("/programme")
def add_programme(programme: Programme):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO programmes VALUES (%s)"
        cursor.execute(sql, (programme.nomProgramme))
        sql_connection.commit()

@router.get("/programme")
def get_programme():
    with sql_connection.cursor() as cursor:
        query = "SELECT nomProgramme FROM programmes"
        cursor.execute(query)
        results = cursor.fetchall()
        return [Programme(nomProgramme=result[0]) for result in results]
    
# inscription
@router.post("/signup")
def post_signup(body: Inscription):
    if not body.email.endswith("@ulaval.ca"):
        raise HTTPException(status_code=400, detail="email must be under @ulaval.ca domain")
    
    # hashage sha256 parce que flemme de bcrypt
    h = hashlib.new('sha256')
    h.update(body.passwd)

    hashed = h.hexdigest()
    
    return True

@router.get("/events")
def get_events():
    with sql_connection.cursor() as cursor:
        query = "SELECT * FROM events"
        cursor.execute(query)
        results = cursor.fetchall()
        return [Events(date=cursor[0], name=cursor[1]) for result in results]
    
@router.get("/billets_achetes")
def get_billets_achetes(nom: str):
    with sql_connection.cursor() as cursor:
        query = "SELECT * FROM vendus WHERE nom = {%s}"
        cursor.execute(query, nom)
        results = cursor.fetchall()
        return [Events(date=cursor[0], nom=cursor[1])]
    
@router.post("/acheter")
def acheter_billet(age:int, numero:int, section:str):
    with sql_connection.cursor() as cursor:
        query = "SELECT prix FROM billet WHERE numero = {%s} AND section = {%s}"
        cursor.execute(query, (numero, section))
        prix = cursor.fetchone()

        if(verifie_age(age)): # On valide le rabais de l'age
            prix = prix - 2
        query = "INSERT INTO vendus (numero, section, prix) VALUES (%s, %s, %s)"
        cursor.execute(query, (numero, section, prix))
        sql_connection.commit()
        
# rien est testé