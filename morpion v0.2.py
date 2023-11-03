grilleTest = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# print la grille
def printgrille ( grille):
    for i in range(3):
        print(grille[i])
        
printgrille(grilleTest)

# commandes du joueur
def commandeJoueur(grille, numeroJoueur):
    while True:
        try:
            saisie_ligne = int(input("Choisissez un nombre entre 1 et 3 pour la ligne: ")) - 1
            saisie_colonne = int(input("Choisissez un nombre entre 1 et 3 pour la colonne: ")) - 1

            if 0 <= saisie_ligne < 3 and 0 <= saisie_colonne < 3 and grille[saisie_ligne][saisie_colonne] == "":
                grille[saisie_ligne][saisie_colonne] = numeroJoueur
                return grille
            else:
                print("Saisie invalide. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

#commandeJoueur(grilleTest, 1)


# check si il y a victoire ou nul
def verification(grille, numeroJoueur):
    """
    vérifie si un même numéro est aligné trois fois de manière diagonale, horizontale ou
    verticale et renvoie un booléen. Si oui il renvoie True sinon il renvoie False
    """
    
    # Vérification en colonne
    for colonne in range(3):
        if grille[0][colonne] == numeroJoueur and grille[1][colonne] == numeroJoueur and grille[0][colonne] == numeroJoueur and grille[2][colonne]:
            return True
    print('Colonne')
    # Vérification en ligne
    for ligne in range(3):
        if grille[ligne][0] == numeroJoueur and grille[ligne][1] == numeroJoueur and grille[ligne][0] == numeroJoueur and grille[ligne][2]:
            return True
    print('Ligne')
    # Vérification en diagonale
    if grille[0][0] == numeroJoueur and grille[1][1] == numeroJoueur and grille[0][0] == numeroJoueur and grille[2][2]:
        return True
    print('diagonale')
    if grille[0][2] == numeroJoueur and grille[1][1] == numeroJoueur and grille[0][2] == numeroJoueur and grille[2][0]:
        return True 
        
    return False
# switch de joueur

def jeu():
    """
    weoihewfoewhfowefihwefeofhewoiewfhweofehwiof
    tests de la fonction

    >>> jeu()
    
    """
    grilleJeu = [
        ["","",""],
        ["","",""],
        ["","",""]
    ]

    Joueuractuel = "X"
    vainqueur = None
    JeuEncours = True
    nombreCases = 0

    while JeuEncours:
        printgrille(grilleJeu)
        print(f"C'est au tour du joueur {Joueuractuel}")
        # Choix du joueur
        grilleJeu = commandeJoueur(grilleJeu, Joueuractuel)
        
        # Augmentation compteur tours
        nombreCases += 1
        
        if verification(grilleJeu, Joueuractuel):
            vainqueur = Joueuractuel
            JeuEncours = False
        elif nombreCases == 9:
            vainqueur = "Nul"
            JeuEncours = False
        else:
            if Joueuractuel == "X":
                Joueuractuel = "O"
            else:
                Joueuractuel = "X"
    
    # Afficher le résultat du jeu
    printgrille(grilleJeu)
    if vainqueur == "Nul":
        print("Le jeu est un match nul!")
    else:
        print(f"Le joueur {vainqueur} a gagné!")
