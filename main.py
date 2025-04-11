# main.py

# Importem FastAPI per crear el servidor web
from fastapi import FastAPI

# Importem BaseModel de Pydantic per validar les dades d'entrada
from pydantic import BaseModel

# Importem json per llegir i escriure dades en format JSON
import json

# Importem os per treballar amb el sistema de fitxers (encara que no el fem servir ara)
import os

# Creem una instància de l'aplicació FastAPI
app = FastAPI()

# Nom del fitxer on es guarden les dades dels alumnes
nom_fitxer = "alumnes.json"

# Definim la classe Alumne per validar les dades rebudes amb POST
class Alumne(BaseModel):
    nom: str
    cognom: str
    data: int
    email: str
    feina: bool
    curs: str
    dia: int
    mes: int
    any: int

# Funció per carregar les dades dels alumnes des del fitxer JSON
def carregar():
    # Obrim el fitxer en mode lectura text
    fitxer = open(nom_fitxer, "rt")
    # Llegim tot el contingut del fitxer com a string
    s = fitxer.read()
    # Tanquem el fitxer
    fitxer.close()
    # Convertim el string JSON a una llista de diccionaris i la retornem
    return json.loads(s)

# Funció per desar les dades dels alumnes al fitxer JSON
def desar():
    # Còpia explícita de la llista per claredat (tot i que no caldria)
    dic = llista_alumnes
    # Convertim la llista a string JSON amb format bonic
    stringJSON = json.dumps(dic, indent=4)
    # Obrim el fitxer en mode escriptura text
    fitxer = open(nom_fitxer, "wt")
    # Escriu el contingut JSON al fitxer
    fitxer.write(stringJSON)
    # Tanquem el fitxer
    fitxer.close()

# Carreguem la llista d’alumnes a partir del fitxer
llista_alumnes = carregar()

# Inicialitzem l’identificador automàtic amb el valor 1
id_actual = 1

# Recorrem la llista d’alumnes per trobar l’últim ID usat
for alumne in llista_alumnes:
    # Si l’ID actual de l’alumne és major o igual que l’actual, l’actualitzem
    if alumne["id"] >= id_actual:
        id_actual = alumne["id"] + 1

# Ruta GET principal que retorna un missatge simple
@app.get("/")
def inici():
    # Retorna una cadena de text
    return "Institut TIC de Barcelona"

# Ruta GET que retorna el nombre total d’alumnes
@app.get("/alumnes/")
def total_alumnes():
    # Retorna un diccionari amb el total d’alumnes
    return {"total": len(llista_alumnes)}

# Ruta GET que retorna un alumne pel seu ID
@app.get("/id/{numero}")
def get_alumne(numero: int):
    # Recorre tots els alumnes de la llista
    for alumne in llista_alumnes:
        # Comprova si l’ID coincideix amb el demanat
        if alumne["id"] == numero:
            # Retorna l’alumne trobat
            return alumne
    # Si no s’ha trobat cap alumne, retorna un missatge d’error
    return {"msg": "Alumne no trobat"}

# Ruta DELETE per eliminar un alumne pel seu ID
@app.delete("/del/{numero}")
def eliminar_alumne(numero: int):
    # Recorre la llista d’alumnes amb índex
    for i, alumne in enumerate(llista_alumnes):
        # Si trobem l’ID a eliminar
        if alumne["id"] == numero:
            # Eliminem l’alumne de la llista
            del llista_alumnes[i]
            # Desa la llista actualitzada al fitxer
            desar()
            # Retorna missatge de confirmació
            return {"msg": "Alumne eliminat"}
    # Si no trobem l’ID, retornem un missatge d’error
    return {"msg": "Alumne no trobat"}

# Ruta POST per afegir un alumne nou
@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    # Convertim l’objecte Alumne a diccionari
    alumne_dict = alumne.dict()
    # Assignem un ID automàtic al nou alumne
    alumne_dict["id"] = len(llista_alumnes) + 1
    # Afegim el nou alumne a la llista
    llista_alumnes.append(alumne_dict)
    # Desa la llista actualitzada al fitxer
    desar()
    # Retorna un missatge de confirmació amb l’ID assignat
    return {"msg": "Alumne afegit", "id": alumne_dict["id"]}
