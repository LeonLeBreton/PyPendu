"""
Crée le 16/12/2021
Dernière modification le 06/01/2022
"""

from random import randint #Utiliser pour la fonction "newWord"
import os #Utiliser pour la fonction "cls"

def cls():
    """
    Permet de supprimer le contenu de la console.
    """
    if os.name in ("nt", "dos"):  #Si sur windows
        clear = "cls"
    else: #Si sur Linux/Unix
        clear = "clear"
    os.system(clear)

def newWord(filePath:str="dicoPendu.txt")->str:
    """
    Prends un mot au hasard dans le dictionnaire (chemin en entrée, par défaut le fichier "dicoPendu.txt" dans le dossier courant).

    La méthode .read() comparée à .readline() lit tous le fichiers et crée une chaine de caractère (str).

    La méthode .readlines() comparée à .readline() lit tous le fichiers et crée une liste (list).
    Les éléments de cette liste sont séparé lors d'un retour à la ligne.
    """
    dico=open(filePath,"r") #Ouvre le dictionnaire
    number = dico.read().count("\n") #Compte nombre de ligne
    dico.seek(0) #Retourne au premier caractère (début du fichier)
    motATrouver = dico.readlines()[randint(1,number)][:-1]
    #[randint(1,number)] permet de récupéré un élément aléatoire dans la liste.
    #[:-1] permet de supprimer le dernier caractère "\n" (python le considère comme un seul caractère) qui permet un retour à la ligne
    dico.close() #Ferme le dictionnaire
    return motATrouver #Renvoie le mot pris au hasard 


def listToStr(liste:list)->str:
    """
    Convertie la liste en chaîne de caractère
    >>> listToStr(["a","b","c"])
    'abc'
    >>> listToStr(["1","2","3"])
    '123'
    >>> listToStr(["A","B","C","d","e","f","1","2","3"])
    'ABCdef123'
    """
    mot=""
    for i in range(len(liste)):
        mot=mot+str(liste[i])
    return mot


def doesInWord(tryletter:str, motATrouver:str):
    """
    Regarde si la lettre est présente dans le mot recherché
    Retourne une chaine de caractère si la lettre est dans le mot, sinon retourne un tuple contenant "bad" et une chaine de caractère contenant la mauvaise lettre
    >>> doesInWord("a", "test")
    ('bad', 'a')
    >>> doesInWord("e","test") 
    'e'
    >>> doesInWord("S","test") #Retourne la lettre en minuscule si la lettre entrée est majuscule
    's'
    >>> doesInWord("u","plusieurs") #Retourne une seul fois la lettre si la lettre est plusieurs fois dans le même mot
    'u'
    >>> doesInWord("t","test")
    't'
    """
    tryletter=tryletter.lower()
    if tryletter in motATrouver:
        return tryletter
    else:
         return "bad", tryletter
    
    
def reveler(lettre:str, searchWord:list, motATrouver:str)->list:
    """
    Remplace les "*" par la lettre rechercher
    >>> reveler("e",["*", "*", "*", "*"], "test")
    ['*', 'e', '*', '*']

    >>> reveler("t",["*", "e", "*", "*"], "test")
    ['t', 'e', '*', 't']

    >>> reveler("s",["t", "e", "*", "t"], "test")
    ['t', 'e', 's', 't']
    
    >>> #Le programme est conçu pour ne pas utiliser cette fonction si la lettre n'est pas dans le mot à trouver
    >>> #Si la fonction est tout de même utiliser, rien ne changera en sortie
    >>> reveler("m",["t", "e", "*", "t"], "test") 
    ['t', 'e', '*', 't']

    >>> #Le programme est également conçu pour ne pas utiliser cette fonction si la lettre est en majuscule
    >>> #Si la fonction est tout de même utiliser, la majuscule ne sera pas transformer en minuscule et rien ne changera en sortie
    >>> reveler("E",["*", "*", "s", "*"], "test")
    ['*', '*', 's', '*']
    """
    liste=list(motATrouver)
    for i in range(len(liste)):
        if liste[i]==lettre:
            searchWord[i]=lettre
    return searchWord


restart=True
while restart:
    #Configuration de début de partie
    victory=False
    motATrouver=newWord() #Crée le nouveau mot
    searchWord=["*"]*len(motATrouver) #Crée une liste composé de * de la longueur du mot
    badLetter=[] #Crée une liste vide destiné à stocker les mauvaises lettres testé
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Alphabet minuscule ASCII
    cls()
    print("Bienvenue dans le Pendu")
    attemps=int(input("Combien d'essai voulez-vous ? : ")) #Demande à l'utilisateur le nombre d'essaie qu'il souhaite. Integer en entrée
    cls()

    #Jeu
    while not attemps==0 and not victory: #Boucle tant que le joueur n'a pas gagné ou perdu
        #Interface utilisateur
        print("Bienvenue dans le Pendu")
        print("Mot à trouver :",listToStr(searchWord))
        print("Mauvais caractères essayés : ",str(badLetter)[1:-1].replace("'","")) # La fonction listToStr n'est pas utilisé car celui-ci ne conserve pas la virgule
        print("Il vous reste {} tentatives".format(attemps))

        check=input("Quel lettre voulez-vous tester ? : ") #Demande une lettre à l'utilisateur
        cls()

        #Vérifie qu'une seul lettre a été entrée
        try:
            check[1]  #Si cette ligne ne crée pas d'erreur, alors il y a plusieurs caractère
            print("Merci de mettre qu'une lettre\n") #!Message d'erreur!

        except IndexError: #Seul un caractère a été entrée
            if check in letter: #Verifie que le caractère entrée est bien une lettre
                tryIt=doesInWord(check, motATrouver) #Plus d'info dans l'aide de la fonction 
                if tryIt[0]=="bad": #Si la lettre n'est pas dans le mot
                    if not tryIt[1] in badLetter: #Verifie que la mauvaise lettre n'a pas déjà été essayer
                        badLetter.append(tryIt[1]) #Ajoute la lettre à la liste des lettres fausses déjà utilisés
                        attemps-=1 #Baisse les chances restantes de 1
                    else: #Si la lettre a déjà été essayé
                        print("Vous avez déjà essayé cette lettre\n") #!Message d'erreur!
                else: #Si la lettre est correct 
                    searchWord = reveler(tryIt,searchWord, motATrouver)
            else:
                print("Merci de mettre une lettre (il n'y a pas d'accent)\n") #!Message d'erreur! Si le caractère n'est pas une lettre

        #Victoire
        if not "*" in listToStr(searchWord): #Quand toutes les lettres ont été révélé (donc plus de *)
            cls()
            victory=True #Permet de ne pas afficher l'écran de défaite
            print("Gagné !")
            print("Mot à trouver :",motATrouver)
            restartChoice = input("Voulez-vous recommencer ? (oui (Par défaut) / non) : ").lower()
            if restartChoice == "non" or restartChoice == "no" or restartChoice == "n": # 3 écritures différentes
                cls()
                restart=False

    #Défaite
    if not victory: 
        cls()
        print("Perdu !")
        print("Le mot était :", motATrouver)
        restartChoice=input("Voulez-vous recommencer ? (oui (Par défaut) / non) : ").lower()
        if restartChoice=="non" or restartChoice=="no" or restartChoice=="n" : # 3 écritures différentes
            cls()
            restart=False