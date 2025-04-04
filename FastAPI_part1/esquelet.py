### Imports ################################################## 
import os   #per neteja la pantalla

#Variables ###################################################

#Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json"

# Mostrar alumnes
alumnes = [
    {"id": 1, "nom": "Akasha", "cognom": "Karam", "data": {"dia": 12, "mes": 5, "any": 2001},
     "email": "akasha.karam@email.com", "feina": True, "curs": "Enginyeria Informàtica"},
    {"id": 2, "nom": "Brithay", "cognom": "Silva", "data": {"dia": 8, "mes": 11, "any": 2000},
     "email": "brithay.silva@email.com", "feina": False, "curs": "Disseny Gràfic"},
    {"id": 3, "nom": "Nerea", "cognom": "Naves", "data": {"dia": 22, "mes": 3, "any": 2002},
     "email": "nerea.naves@email.com", "feina": True, "curs": "Psicologia"},
    {"id": 4, "nom": "Adriana", "cognom": "Sanchez", "data": {"dia": 15, "mes": 7, "any": 1999},
     "email": "adriana.sanchez@email.com", "feina": False, "curs": "Administració d'Empreses"},
    {"id": 5, "nom": "Alex", "cognom": "Moreno", "data": {"dia": 30, "mes": 9, "any": 2003},
     "email": "alex.moreno@email.com", "feina": True, "curs": "Matemàtiques"},
    {"id": 6, "nom": "Mario", "cognom": "Mosquera", "data": {"dia": 5, "mes": 2, "any": 2001},
     "email": "mario.mosquera@email.com", "feina": False, "curs": "Història"},
    {"id": 7, "nom": "Alejandro", "cognom": "Muñoz", "data": {"dia": 17, "mes": 6, "any": 2000},
     "email": "alejandro.munoz@email.com", "feina": True, "curs": "Enginyeria Mecànica"},
]

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
        case "1":
                os.system('cls')
                print("Mostrar alumnes")
                print("-------------------------------")


                #Introduiu el vostre codi per mostrar alumnes aquí
                print("[1] Akasha Karam")


                input()

            # Afegir alumne ##################################
            case "2":
                os.system('cls')
                print("Afegir alumne")
                print("-------------------------------")

                #Introduiu el vostre codi per afegir un alumne aquí

                input()

            # Veure alumne ##################################
            case "3":
                os.system('cls')
                print("Veure alumne")
                print("-------------------------------")

                #Introduiu el vostre codi per veure un alumne aquí

                input()

            # Esborrar alumne ##################################
            case "4":
                os.system('cls')
                print("Esborrar alumne")
                print("-------------------------------")

                #Introduiu el vostre codi per esborrar un alumne aquí

                input()

            # Desar a fitxer ##################################
            case "5":
                os.system('cls')
                print("Desar a fitxer")
                print("-------------------------------")

                #Introduiu el vostre codi per desar a fitxer aquí

                input()

            # Llegir fitxer ##################################
            case "6":
                os.system('cls')
                print("Llegir fitxer")
                print("-------------------------------")

                #Introduiu el vostre codi per llegir de fitxer aquí

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
