import numpy as np

#i, j
board = np.array([
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 2, 1, 1, 4, 1, 1, 2, 3, 2, 1, 1, 4, 1, 1, 2, 3, 2, 1, 1, 4, 1, 1, 2, 3, 2, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
    [2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
    [2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 1, 1, 2, 5, 2, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],


])

characters = {
	0: ' ',
	1: '.',
	2: '|',
    3: 'O',
    4: ':',
    5: 'X'
	}

def Print_board():
    for row in board:
        for col in row:
            print(characters[col], end='')
        print()


def Move():
    # Position de départ
    i = 8
    j = 9

    # 5 = 'X', position du joueur
    joueur = 5
    pos = board[i, j]

    while True:
        
        print('''
            Tapez H pour monter
            Tapez B pour descendre
            Tapez G pour aller à gauche
            Tapez D pour allez à droite''')
        if i == 2 and (j == 1 or j == 17) :
            print('''   \t    Tapez S pour prendre le couloir spécial''') # si le joueur se situe dans une des deux cases possible, il a une option supplementaire
        if i == 2 and (j == 25 or j == 17) : # si le joueur se situe dans une des deux cases possible, il a une option supplementaire lui permettant de finir
            print('''   \t    Tapez F pour FINIR''')
        dir = input().lower()

        #Enregistrement de la position avant de se déplacer (pour pouvoir la remettre à sa valeur de base)
        prev_i, prev_j = i, j
        prev_pos = pos
        
        if dir == "s" and i == 2 and (j == 17): # si le joueur ecrit "s" et qu'il est dans les conditions necessaires il prendra le couloir special
            j -= 16

        if dir == "s" and i == 2 and (j == 1): # idem 
            j += 16

        if dir == "f" and i == 2 and (j == 25 or j == 17) : # si le joueur ecrit "f" et qu'il est dans les conditions necessaires
            i = 0                                           #  il finira dans la case finale
            j = 21
        if dir == "h":
            i -= 2
        elif dir == "b":
            i += 2
        elif dir == "g":
            j -= 8
        elif dir == "d":
            j += 8

        # Vérifier que la nouvelle position respecte les limites de la carte
        # On vérifie que l'indice est compris entre 0 et le nb de lignes (board.shape[0]) pour i et entre 0 et le nombre de colonnes (board.shape[1]) pour j
        if (0 <= i < board.shape[0]) and (0 <= j < board.shape[1]):
            pos = board[i, j] 
        else:
            # Si ça dépasse les limites, on revient à la position précédente
            i, j, pos = prev_i, prev_j, prev_pos
            print ("vous ne pouvez pas allez plus loin dans cette direction")

# -------------------------------------------------------
        #if i == 0 :                                        j'ai supprimé cette ligne car elle me bloquait pour me deplacer a la piece finale
        #    i, j, pos = prev_i, prev_j, prev_pos           
# ------------------------------------------------------

        # Mise à jour de la position précédente pour la remettre à sa valeur de base
        board[prev_i, prev_j] = prev_pos
        board[i, j] = joueur
        board[8, 9] = 3

        Print_board()

#CODE PRINCIPAL 

regles = '''A chaque tour, le fantome peut se déplacer dans une pi`ece/case contigüe à la case dans lequel il se trouve. 
Cette case peut contenir de l'énergie sous forme de pintes d’ectoplasme vert ou bien un ennemi.

Liste des ennemis :
• Le maitre du chateau - qui veut garder le fantôme car c’est une bonne attraction touristique - il renvoie le
fantôme dans la case reception. Lorsque le fantôme est `a 1 case du maitre du chateau il entend les cl`es de son
trousseau.
• Le savant fou, prend 1 pinte d’´energie et transporte Gasper dans une case de son choix. Lorsque le fantôme est
à une case du savant il entend son rire sardonique.
• 3 Bibbendum Chamallow - il déverse sa mousse sur le fantôme et le paralyse en lui prenant 2 pintes d’énergie.
Lorsque le fantôme est à une case du Bibbendum il sent l’odeur alléchante du chamallow fraise'''

print("----------\nBienvenue!\n----------")
print("RÈGLES DU JEU : ", regles)


print("----------\nTAPEZ 1 POUR JOUER :\n----------")
rep = int(input())
if rep == 1:
    Print_board()
    Move()
