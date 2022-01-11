from tkinter import *
from random import randint

try : #Télécharge le dictionnaire si il n'est pas présent sur le pc
    open("dicoPendu.txt","x") # "x" -> Permet de vérifier la présence du fichier. Si le fichier existe, il y aura l'erreur "FileExistsError"
    import requests
    file = open("dicoPendu.txt","w")
    response = requests.get('https://gist.githubusercontent.com/LeonLeBreton/6e735da42ddd34404c5fa7b1d1abbe25/raw/b4d39fdb6386a3f5660ed01c78a62fc08fedbc1e/gistfile1.txt')
    file.write(response.text)
    file.close()

except FileExistsError: #Ne fais rien si il existe
    pass

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


####################################################################################
def dessin(dessinStatue):
    """
    dessinStatues[0] = la progression du dessin
    dessinStatues[1] = difficulté (8 : facile, 6 : moyen, 4 : difficile)
    Facile    : 1,2,3,4,5,6,7,8
    Moyen     : 1,2,3,4,6,8
    Difficile : 1,3,4,8

    Impossibilité d'utiliser "elif" car parfois plusieurs "if" sont nécessaire
    """
    if dessinStatue[0]==1:
        canv.create_line(50, 280, 150, 280, width=5)    #1/1/1

    if dessinStatue[0]==2:
        canv.create_line(100, 280, 100, 130, width=5)   #2/2/2        

    if dessinStatue[0]==3 and not dessinStatue[1]==4 or dessinStatue[0]==2 and dessinStatue[1]==4:
        canv.create_line(100, 130, 200, 130, width=5)   #3/3/2
        
    if dessinStatue[0]==4 and not dessinStatue[1]==4 or dessinStatue[0]==3 and dessinStatue[1]==4:
        canv.create_line(200, 130, 200, 160, width=5)   #4/4/3
        
    if dessinStatue[0]==5 and not dessinStatue[1]==4 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_oval(180, 160, 220, 200, width=5)   #5/5/4        

    if dessinStatue[0]==6 and dessinStatue[1]==8 or dessinStatue[0]==5 and dessinStatue[1]==6 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_line(200, 200, 200, 250, width=5)   #6/5/4
        
    if dessinStatue[0]==7 and dessinStatue[1]==8 or dessinStatue[0]==6 and dessinStatue[1]==6 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_line(180, 225, 220, 225, width=5)   #7/6/4        

    if dessinStatue[0]==8 and dessinStatue[1]==8 or dessinStatue[0]==6 and dessinStatue[1]==6 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_line(200, 250, 220, 260, width=5)   #8/6/4
        canv.create_line(200, 250, 180, 260, width=5)

def endGame(statues, motATrouver):
    """
    Fonction gérant la fin du jeu et le recommencement d'une possible nouvelle partie
    """
    #Supression d'éléments du jeu
    Hint      .place_forget()
    Letter    .place_forget()
    InCorrect .place_forget()
    SearchWord.place_forget()

    if statues == "loose": #Si le joueur a perdu
        EndGame.config(text= "Perdu !", fg= "red")
    else: #Sinon (Si le joueur a gagné)
        EndGame.config(text= "Gagné !", fg= "blue")

    WordIs.config(text= "Le mot était : {}".format(motATrouver)) #Donne la solution
    WordIs.place (x= 0,   y= 240, width= 550, height= 80 )
    EndGame.place(x= 0,   y= 150, width= 550, height= 120)
    Restart.place(x= 100, y= 340, width= 350, height= 100)

def event(evt, motATrouver, searchWord, badLetter,allLetter,totalAttemps):
    """
    Activer lorsque une touche est presser.
    Fonction principal du fonctionnement du jeu
    """
    global actualLetter #Lettre précédement appuyer
    global attemps #Essai restant
    global dessinStatue #Statue actuel du dessin dans le canvas

    InCorrect.config(text= "") #Enlève le précédent "Correct" ou "Incorrect"
    Letter   .config(fg= "black") #Remet le texte dans sa couleur d'origine
    pressed = evt.keysym #Met la touche pressé dans une variable
    if pressed == "Return" and "actualLetter" in globals(): #Verifie la variable "actualLetter" (existe si une nouvelle lettre a été entrée) existe lorsque la touche entrée est appuyer
        tryIt = doesInWord(actualLetter, motATrouver) #Utilisation de la fonction "doesInWord()", "actualLetter" utilisé dans cette fonction existe forcément grâce à la vérification au dessus
        if tryIt[0]=="bad": #Si la lettre est pas dans le mot
                allLetter.append(tryIt[1]) #Ajoute la lettre dans la liste des lettres essayés 
                badLetter.append(tryIt[1]) #Ajoute la lettre dans la liste des lettres mauvaises essayés 
                attemps-=1 #Retire un essai du compteur
                forUserAttemps = str(attemps-totalAttemps).replace("-","") #Met à jour le nombre d'essai restant compteur affiché
                CurrentError.config(text= "{0}/{1} erreurs".format(forUserAttemps,totalAttemps)) #Met à jour le compteur affiché
                BadLetter   .config(text= badLetter) #Met à jour la liste des mauvaises lettre essayé
                InCorrect   .config(text= "Incorrect !", fg="red") # Affiche le texte "Incorrect" en rouge en dessous de la lettre
                Letter      .config(fg= "red") #Met la lettre incorrect en rouge
                dessin(dessinStatue) #Met à jour le dessin
                dessinStatue[0]+=1 #Incrément le compteur du dessin de 1
                if attemps == 0: #Perdu, lorsque il n'y a plus d'essai
                    endGame("loose", motATrouver)
        else: #Lorsque la lettre est bonne
            allLetter.append(tryIt) #Ajoute la lettre dans la liste des lettres essayés 
            searchWord:list = reveler(tryIt, searchWord, motATrouver) #Se référer à l'aide de la fonction
            SearchWord.config(text= listToStr(searchWord)) #Met à jour les étoiles pour afficher les nouvelles lettre
            InCorrect .config(text= "Correct !", fg= "green") #Affiche le texte "Correct" en vert en dessous de la lettre
            Letter    .config(fg= "green") #Met la lettre en vert
            if not "*" in searchWord: #Gagné, si il n'y a plus de lettre non trouvé
                endGame("win", motATrouver)
        del actualLetter #Supprime la lettre essayé 
        
    elif pressed in allLetter: #Si la lettre est dans la liste des lettres essayé
        Letter.config(text="Lettre déjà testé")
        if "actualLetter" in globals():
            del actualLetter
        
    elif pressed in letter: #Lorsque une lettre est presser 
        Letter.config(text=pressed.upper()) #Affiche la lettre a l'utilisateur (en majuscule pour un meilleur rendu)
        actualLetter = pressed #Met la lettre en mémoire


def game(difficulty:str, difficultyColor:str, attempsVar:int):
    """
    Lorsque la partie commence.
    Cette fonction ne gère pas le cours du jeu, elle place seulement les éléments et crée la configuration initial
    Elle supprime également les bouttons du menu principal
    """
    global attemps
    global dessinStatue

    motATrouver:str  = newWord() #Crée un nouveau mot
    searchWord:list   = ["*"]*len(motATrouver)
    badLetter:list    = [] #Liste des mauvaises lettre testé
    allLetter:list    = [] #Liste des lettres testé
    totalAttemps = attemps = attempsVar #Création de la variable totalAttemps qui est le nombre total d'essai possible et la variable attemps qui est un compteur du nombre d'essai restant
    dessinStatue = [1,attempsVar] #Variable servant au dessin, plus d'informatique dans l'aide de la fonction "dessin"

    #Suppression des boutons/textes du menu principal
    Welcome    .place_forget()
    Difficulty .place_forget()
    Easy       .place_forget()
    Medium     .place_forget()
    Hard       .place_forget()

    #Left
    SearchWord         .config(text= listToStr(searchWord))
    SelectedDifficulty .config(text= "Difficulté : {}".format(difficulty), fg= difficultyColor)

    SearchWord.place         (x= 0, y= 100, width= 550, height= 100)
    Hint.place               (x= 0, y= 270, width= 550, height= 25 )
    SelectedDifficulty.place (x= 0, y= 0,   width= 550, height= 95 )
    InCorrect.place          (x= 0, y= 430, width= 550, height= 25 )
    Letter.place             (x= 0, y= 320, width= 550, height= 75 )

    #Jeu
    win.bind_all('<Key>', lambda evt: event(evt, motATrouver, searchWord, badLetter,allLetter, totalAttemps))

    #Right
    canv.place       (x= 550, y= 0)
    canv.create_line (0, 0, 0, 500, width= 5)

    CurrentError .config(text="0/{} erreurs".format(totalAttemps))
    CurrentError .place(x= 553, y= 10,  width= 230, height= 30)
    BadLetterHint.place(x= 553, y= 325, width= 350, height= 65)
    BadLetter    .place(x= 553, y= 370, width= 350, height= 120)


#Main menu
def mainMenu():
    """
    Menu principal
    Fonction utiliser au début du programme et à la fin d'une partie lorsque le bouton "Recommencer" est pressé.
    
    Déroulement de la fonction :
        -Commence par retirer/réinitialisé les boutons potentiel/texte/canv de l'ancienne partie si il y en a eu une.
        -Affiche les textes du menu principal et les boutons de choix de difficulté.
    """
    #Supprime ce qui c'est passée avant
    SelectedDifficulty.place_forget()
    SearchWord        .place_forget()
    InCorrect         .place_forget()
    EndGame           .place_forget()
    Restart           .place_forget()
    WordIs            .place_forget()
    Hint              .place_forget()
    canv              .place_forget()
    CurrentError      .place_forget()
    BadLetterHint     .place_forget()
    BadLetter         .place_forget()
    canv              .delete(ALL)

    Letter   .config (text= "", fg= "black")
    BadLetter.config (text= "")
    InCorrect.config (text= "")
    
    Welcome.place   (x= 0,   y= 30 , width= 900, height= 120)
    Difficulty.place(x= 0,   y= 200, width= 900, height= 100)
    Easy.place      (x= 120, y= 300, width= 170, height= 160)
    Medium.place    (x= 340, y= 300, width= 170, height= 160)
    Hard.place      (x= 560, y= 300, width= 170, height= 160)

#Global variable
letter  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Alphabet minuscule ASCII

#Fenêtre
win = Tk()
win.title ("Pendu")
win.geometry("900x500")
win.resizable (width = False , height = False)

#Left
SelectedDifficulty = Label (win, justify= "center", font= ("Arial","28"))
SearchWord         = Label (win, justify= "center", font= ("Arial","48"))
Letter             = Label (win, justify= "center", font= ("Arial","33"))
InCorrect          = Label (win, justify= "center", font= ("Arial","22"))
EndGame            = Label (win, justify= "center", font= ("Arial","35"))
WordIs             = Label (win, justify= "center", font= ("Arial","30"))
Hint               = Label (win, justify= "center", font= ("Arial","18"), text = "Appuyer sur une lettre puis sur Entrée pour valider")
Restart            = Button(win, justify= "center", font= ("Arial","35"), text="Recommencer", bg= "#121235", fg= "white", command= mainMenu)

#Right
canv          = Canvas(win, width = 350, height=500)
CurrentError  = Label (win, font= ("Arial","22"))
BadLetterHint = Label (win, text= "Mauvaise lettre :", justify= "center", font= ("Arial","28"))
BadLetter     = Label (win, justify= "center", font= ("Arial","24"))

#Main Menu
Welcome    = Label (win, text = "Bienvenue dans le pendu"    , justify= "center", font= ("Arial","38"))
Difficulty = Label (win, text = "Choisissez votre difficulté", justify= "center", font= ("Arial","22"))

Easy       = Button(win, text = "8 erreurs", justify= "center", font= ("Arial","16"), bg= "#4975B7", command= lambda:game("Facile"   , "#4975B7", 8))
Medium     = Button(win, text = "6 erreurs", justify= "center", font= ("Arial","16"), bg= "#1A6300", command= lambda:game("Moyen"    , "#1A6300", 6))
Hard       = Button(win, text = "4 erreurs", justify= "center", font= ("Arial","16"), bg= "#FF3701", command= lambda:game("Difficile", "#FF3701", 4))


mainMenu()
win.mainloop()
