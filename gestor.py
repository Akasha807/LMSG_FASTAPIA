### Imports ################################################## 
import os   # per netejar la pantalla
import json

### Variables ###################################################

# Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json"

# Inicialitzem la llista d’alumnes buida
alumnes = []


### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()



### Programa ################################################

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")

            # Mostra per pantalla la llista d'alumnes amb el seu identificador, nom i cognom.
            # S'assumeix que 'alumnes' és una llista de diccionaris amb les claus "id", "nom" i "cognom".
            for i in alumnes:
                print(i["id"], i["nom"], i["cognom"])
        

            input()
    
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per afegir un alumne aquí

            # Generar nou ID incremental
            nou_id = 0  # Inicialitzem a 0 per si no hi ha alumnes

            # Busquem l'ID més alt existent
            for alumne in alumnes:
                if alumne['id'] > nou_id:
                    nou_id = alumne['id']

            # Incrementem per al nou alumne
            nou_id += 1

            # Demanem dades del nou alumne
            nou_alumne = {
                "id": nou_id,
                "nom": input("Introdueix el nom: "),
                "cognom": input("Introdueix el cognom: "),
                "data": {
                    "dia": int(input("Dia de naixement: ")),
                    "mes": int(input("Mes de naixement: ")),
                    "any": int(input("Any de naixement: "))
                },
                "email": input("Introdueix l'email: "),
                "feina": input("Treballa? (S/N): ").upper() == "S",
                "curs": input("Introdueix el curs: ")
            }

            # Afegim el nou alumne a la llista
            alumnes.append(nou_alumne)
            print("Alumne afegit correctament amb ID: {nou_id}")

            input()
    
        # Veure alumne

        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")

            # Mostra un missatge demanant a l'usuari que introdueixi l'identificador d'un alumne.
            print("ID del alumno:")

            # Llegeix l'ID introduït per l'usuari i el converteix a enter.
            id = int(input())

            # Recorre la llista d'alumnes per cercar aquell que tingui l'ID introduït.
            for alumne in alumnes:

                # Si es troba un alumne amb l'ID corresponent, es mostra tota la seva informació.
                if alumne["id"] == id:
                    print(alumne)

            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")

            # Demana a l'usuari que introdueixi l'ID de l'alumne que vol eliminar.
            id = int(input())

            # Inicialitzem una variable booleana per saber si hem trobat l'alumne.
            trobat = False

            # Recorrem la llista d'alumnes amb un bucle que utilitza l'índex.
            for i in range(len(alumnes)):

                # Comprovem si l'ID de l'alumne actual coincideix amb l'ID introduït.
                if alumnes[i]["id"] == id:
                    # Si coincideix, eliminem l'alumne de la llista amb pop(i) i guardem les seves dades.
                    alumne_eliminat = alumnes.pop(i)

                    # Mostrem un missatge confirmant l'eliminació i les dades de l'alumne eliminat.
                    print(f"S'ha eliminat l'alumne: {alumne_eliminat}")

                    # Marquem que hem trobat l'alumne i sortim del bucle.
                    trobat = True
                    break

            # Si no hem trobat cap alumne amb l'ID indicat, informem a l'usuari.
            if not trobat:
                print("No s'ha trobat cap alumne amb aquest ID")

            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per desar a fitxer aquí

            # obrim el fitxer per escriure
            fitxer = open("alumnes.json", "wt")

            # Passem el diccionari a string
            stringJSON = json.dumps(alumnes)

            # Ho escrivim al fitxer
            fitxer.write(stringJSON)

            # i tanquem
            fitxer.close()

            input()

        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            #Obrim fitxer per lectura
            fitxer = open ("alumnes.json", "rt")

            #Llegim el fitxer a un string
            s = fitxer.read()

            #El carreguem a un diccionari
            alumnes = json.loads(s)

            #i tanquem
            fitxer.close()

            input()

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input()
