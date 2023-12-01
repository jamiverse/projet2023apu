
board = [
    [15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 17, 13, 17, 15, 15, 15, 15, 15, 15, 15],
    [15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 15],
    [17, 9, 17, 16, 16, 18, 16, 16, 17, 10, 17, 16, 18, 16, 16, 17, 11, 17, 16, 18, 16, 16, 17, 12, 17, 15, 15, 15, 15, 15],
    [15, 18, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 18, 15, 15, 15, 15],
    [17, 5, 17, 16, 16, 18, 16, 16, 17, 6, 17, 16, 16, 18, 16, 16, 17, 7, 17, 16, 16, 18, 16, 16, 17, 8, 17, 15, 15, 15],
    [15, 18, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 18, 15, 15, 15, 15],
    [17, 1, 17, 16, 16, 18, 16, 16, 17, 2, 17, 16, 16, 18, 16, 16, 17, 3, 17, 16, 16, 18, 16, 16, 17, 4, 17, 15, 15, 15],
    [15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
    [15, 15, 15, 15, 15, 18, 16, 16, 17, 0, 17, 16, 16, 18, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
]




characters = {
    #Dessin
    15: ' ',
    16: '.',
    17: '|',
    18: ':',
    19: 'X',

    #Pièces
    13: 'E',
    12: 12,
    11: 11,
    10: 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2,
    1: 1,
    0: 0

}

def Menu():
    regles = '''A chaque tour, le fantome peut se déplacer dans une pièce/case contigüe à la case dans lequel il se trouve. 
    Cette case peut contenir de l'énergie sous forme de pintes d’ectoplasme vert ou bien un ennemi.

    Liste des ennemis :
    • Le maitre du chateau - qui veut garder le fantôme car c’est une bonne attraction touristique - il renvoie le
    fantôme dans la case reception. Lorsque le fantôme est à 1 case du maitre du chateau il entend les clés de son
    trousseau.
    • Le savant fou, prend 1 pinte d’énergie et transporte Gasper dans une case de son choix. Lorsque le fantôme est
    à une case du savant il entend son rire sardonique.
    • 3 Bibbendum Chamallow - il déverse sa mousse sur le fantôme et le paralyse en lui prenant 2 pintes d’énergie.
    Lorsque le fantôme est à une case du Bibbendum il sent l’odeur alléchante du chamallow fraise'''

    print("----------\nBienvenue!\n----------")
    print("RÈGLES DU JEU : ", regles)

#write a function that prints the board
def print_board(board, characters):
    for row in board:
        for cell in row:
            print(characters[cell], end="")
        print()



def Info(salles):
    for i in range(14):
        salles[i] = {
            "voisins": '',
            "savant": False,
            "maitre" : False,
            "chamallow" : False,
            "pintes": False,
            "joueur": False
        }

    


def Voisins(salles):
    salles[0]['voisins'] = [1, 2, 3]
    salles[1]['voisins'] = [0, 2, 5, 6]
    salles[2]['voisins'] = [0, 1, 3, 5, 6, 7]
    salles[3]['voisins'] = [0, 2, 4, 6, 7, 8]
    salles[4]['voisins'] = [3, 7, 8]
    salles[5]['voisins'] = [1, 2, 6, 9, 10]
    salles[6]['voisins'] = [1, 2, 3, 5, 7, 9, 10, 11]
    salles[7]['voisins'] = [2, 3, 4, 6, 8, 10, 11, 12]
    salles[8]['voisins'] = [3, 4, 7, 11, 12]
    salles[9]['voisins'] = [5, 6, 10, 11]
    salles[10]['voisins'] = [5, 6, 7, 9, 11]
    salles[11]['voisins'] = [6, 7, 8, 9, 10, 12, 13]
    salles[12]['voisins'] = [7, 8, 11, 13]
    salles[13]['voisins'] = [11, 12]





def Move(salles, board, rows, cols,personnage_HP):
    joueur = 19
   

    for i in range(14):
        if salles[i]["joueur"]:
            board[rows[i]][cols[i]] = joueur
            print_board(board, characters)
            print("\nVous êtes dans la salle", i,)
            # if salles[i]["pintes"]
            print ("Vous avez",personnage_HP," pintes d'energies\n")
            voisins_son(salles)
            print("\nVous pouvez vous déplacer dans les salles suivantes :", salles[i]["voisins"])
            print("Dans quelle salle souhaitez-vous vous déplacer ?\n")
            choix = int(input())

            if choix in salles[i]["voisins"]:
                salles[i]["joueur"] = False
                salles[choix]["joueur"] = True
                print("\n\n\n\n\n\n\n\nVous vous deplacer dans la salle", choix,"\n")
                if salles[choix]["maitre"] == True :
                    print("Malheureusement, vous entrez entré dans la piece du Maitre du chateau... Vous retournez donc à la reception\n")
                if salles[choix]["savant"] == True :
                    print("Malheureusement, vous entrez dans la piece du Savant... Vous perdez une pinte et vous vous faites deplacer dans une piece aléatoire\n")
                if salles[choix]["chamallow"] == True :
                    print("Malheureusement, vous entrez entré dans la piece d'un Bibbendum... Vous perdez donc 2 pintes\n")
                if salles[choix]["pintes"] == True :
                    print("Vous avez de la chance, vous entrez dans une piece contenant des pintes, vous recuperez entre 1 et 3 pintes\n")
            else:
                print("\n\n\n\n\n\n\n\nVous ne pouvez pas vous déplacer dans cette salle.\n")
            board[rows[i]][cols[i]] = i
            return salles, personnage_HP
        
# ------------------------------------------------------------------ 

def placement_items(salles) :
    # PLACEMENT MECHANT
    salles_chamallow = random.sample(range(1,13),3)
    for i in range (3) :
        salles[salles_chamallow[i]]["chamallow"] = True
    salle_maitre = random.randint(1,12)
    while salle_maitre in salles_chamallow :
        salle_maitre = random.randint(1,12)
    salles[salle_maitre]["maitre"] = True
    salle_savant = random.randint(1,12)
    while salle_maitre == salle_savant or salle_savant in salles_chamallow :
        salle_savant = random.randint(1,12)
    salles[salle_savant]["savant"] = True

    # PLACEMENT PINTES
    salles_utilisées = []
    salles_utilisées = salles_chamallow + [salle_maitre, salle_savant]
    salles_pintes = random.sample(range(1,13),5)
    for i in salles_pintes :
        while i in salles_utilisées :
            i = random.randint(1,12)
        salles[i]["pintes"] = True
        salles_utilisées.append(i)

def Savant_fou (salles,personnage_HP):
    personnage_HP  = personnage_HP - 1
    if personnage_HP > 0 :
        print ("Vous avez perdu 1 pintes d'energies\n")
    
    for i in range (14) : 
        if salles[i]["joueur"] == True:
            salle_savant = i
            salles[i]['joueur'] = False # supprime le joueur de la case actuelle

    numero_salle = random.randint(0,13)
    while numero_salle == salle_savant :
         numero_salle = random.randint(0,13)
    salles[numero_salle]["joueur"] = True
    return personnage_HP


def Maitre_chateau (salles) :
    for i in range(14):
        if salles[i]["joueur"] == True:
             salles[i]['joueur'] = False # supprime le joueur de la case actuelle

    salles[0]['joueur'] = True # renvoie le joueur a la case depart
    


def Chamallow (personnage_HP):
    personnage_HP = personnage_HP - 2
    if personnage_HP > 0 :
        print ("Vous avez perdu 2 pintes d'energies\n")
    return personnage_HP

def meet_items(salles,personnage_HP) :
    for i in range(1,13) :
        if salles[i]["joueur"] == True :
            if salles[i]["chamallow"] == True :
                personnage_HP = Chamallow(personnage_HP)
            if salles[i]["maitre"] == True :
                Maitre_chateau(salles)
            if salles[i]["savant"] == True :
                personnage_HP = Savant_fou(salles,personnage_HP)
            if salles[i]["pintes"] == True :
                personnage_HP = personnage_HP + random.randint(1,3)
                salles[i]["pintes"] = False
    return personnage_HP
    
def voisins_son(salles) :
    for i in range(13) :
        if salles[i]["joueur"] == True :
            for j in salles[i]["voisins"] :
                if salles[j]["maitre"] == True :
                    print("Vous entendez le bruit d'un trousseau de clés...")
                if salles[j]["chamallow"] == True :
                    print("Vous sentez l'odeur alléchante de chamallow fraise...")
                if salles[j]["savant"] == True : 
                    print("Vous entendez un rire sardonique...")

# --------------------------------------------------------------------------------------------------


# CODE PRINCIPAL
import random
salles = {}

rows = [8, 6, 6, 6, 6, 4, 4, 4, 4, 2, 2, 2, 2, 0]
cols = [9, 1, 9, 17, 25, 1, 9, 17, 25, 1, 9, 16, 23, 21]


Info(salles)
Menu()

Voisins(salles)
salles[0]["joueur"] = True
personnage_HP = 3
placement_items(salles)

while salles[13]["joueur"] == False:
    Move(salles, board, rows, cols, personnage_HP)
    personnage_HP = meet_items(salles,personnage_HP)
    if personnage_HP <= 0:
        break
if personnage_HP <= 0: 
    print ("\n\n\nVous avez perdu !\n\n\n")
if salles[13]["joueur"] == True:
    print("\n\n\n\nVous avez gagné !\n\n\n")
