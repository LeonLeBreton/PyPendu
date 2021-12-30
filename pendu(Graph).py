from tkinter import *
from random import randint
import requests

#******************Création de la fenêtre************
#****************************************************
win = Tk()                            # Fenêtre nommée win
win.title ("Pendu")  # Titre
win.geometry("900x500")               # Dimension de la fenêtre
win.resizable (width = False , height = False)
#********************************************************

try : #Télécharge le dictionnaire si il n'est pas présent sur le pc
    open("dicoPendu.txt","x") # "x" -> Permet de vérifier la présence du fichier. Si le fichier existe, il y aura l'erreur "FileExistsError"
    file = open("dicoPendu.txt","w")
    response = requests.get('https://gist.githubusercontent.com/LeonLeBreton/6e735da42ddd34404c5fa7b1d1abbe25/raw/b4d39fdb6386a3f5660ed01c78a62fc08fedbc1e/gistfile1.txt')
    file.write(response.text)
    file.close()

except FileExistsError: #Ne fais rien si il existe
    pass

def newWord(filePath:str="dicoPendu.txt")->str:
    """
    Prends un mot au hasard dans le dictionnaire
    """
    motATrouver=""
    dico=open(filePath,"r")
    number = dico.read().count("\n") #Compte nombre de ligne
    print(number)
    dico.close()

    dico=open(filePath,"r")
    for i in range(randint(1,number)):
        motATrouver = dico.readline()[:-1]
    dico.close()
    return motATrouver

def listToStr(liste:list)->str:
    """
    Convertie la liste en chaîne de caractère
    >>> listToStr(["a","b","c"])
    'abc'
    >>> listToStr(["1","2","3"])
    '123'    
    """
    mot=""
    for i in range(len(liste)):
        mot=mot+str(liste[i])
    return mot

def doesInWord(tryletter:str, motATrouver):
    """
    Regarde si la lettre est présente dans le mot recherché
    """
    tryletter=tryletter.lower()
    if tryletter in motATrouver:
        return tryletter
    else:
         return "bad",tryletter

def reveler(lettre:str, motATrouver:str, searchWord:list)->list:
    """
    Remplace les "*" par la lettre rechercher
    """
    liste=list(motATrouver)
    for i in range(len(liste)):
        if liste[i]==lettre:
            searchWord[i]=lettre
    return searchWord

####################################################################################
def dessin():
    """
    dessinStatues[0] = la progression du dessin
    dessinStatues[1] = difficulté (8 : facile, 6 : moyen, 4 : difficile)
    Facile    : 1,2,3,4,5,6,7,8
    Moyen     : 1,2,3,4,6,8
    Difficile : 1,3,4,8

    Impossibilité d'utiliser "elif" car parfois plusieurs "if" sont nécessaire
    """
    global dessinStatue
    if dessinStatue[0]==1:
        canv.create_line(50, 280, 150, 280, width=5)    #1/1/1
        

    if dessinStatue[0]==2:
        canv.create_line(100, 280, 100, 130, width=5)   #2/2/2        

    if dessinStatue[0]==3 and not dessinStatue[1]==4 or dessinStatue[0]==2 and dessinStatue[1]==4:
        canv.create_line(100, 130, 200, 130, width=5)   #3/3/2
        

    if dessinStatue[0]==4 and not dessinStatue[1]==4 or dessinStatue[0]==3 and dessinStatue[1]==4:
        canv.create_line(200, 130, 200, 160, width=5)   #4/4/3
        

    if dessinStatue[0]==5 and not dessinStatue[1]==4 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_oval(180,160, 220, 200, width=5)    #5/5/4        

    if dessinStatue[0]==6 and dessinStatue[1]==8 or dessinStatue[0]==5 and dessinStatue[1]==6 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_line(200,200, 200, 250, width=5)    #6/5/4
        

    if dessinStatue[0]==7 and dessinStatue[1]==8 or dessinStatue[0]==6 and dessinStatue[1]==6 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_line(180,225, 220, 225, width=5)    #7/6/4        

    if dessinStatue[0]==8 and dessinStatue[1]==8 or dessinStatue[0]==6 and dessinStatue[1]==6 or dessinStatue[0]==4 and dessinStatue[1]==4:
        canv.create_line(200,250,220,260, width=5)      #8/6/4
        canv.create_line(200,250,180,260, width=5)

    dessinStatue[0]+=1

def endGame(statues, motATrouver):
    Hint      .place_forget()
    Letter    .place_forget()
    InCorrect .place_forget()
    SearchWord.place_forget()
    if statues=="loose":
        EndGame.config(text="Perdu !", fg="red")
    else:
        EndGame.config(text="Gagné !",fg="blue")
    WordIs.config(text="Le mot était : {}".format(motATrouver))
    WordIs.place(x=0,y=240,width=550,height=80)
    EndGame.place(x=0,y=150,width=550,height=120)
    Restart.place(x=100,y=340,width=350,height=100)

def event(evt, motATrouver, searchWord, badLetter,allLetter,totalAttemps):
    global actualLetter
    global attemps

    InCorrect.config(text="")
    Letter   .config(fg="black")
    pressed=evt.keysym
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if pressed=="Return" and "actualLetter" in globals():
        tryIt=doesInWord(actualLetter, motATrouver)
        if tryIt[0]=="bad":
                allLetter.append(tryIt[1])
                badLetter.append(tryIt[1])
                attemps-=1
                forUserAttemps = str(attemps-totalAttemps).replace("-","")
                CurrentError.config(text= "{0}/{1} erreurs".format(forUserAttemps,totalAttemps))
                BadLetter   .config(text= badLetter)
                InCorrect   .config(text= "Incorrect !", fg="red")
                Letter      .config(fg= "red")
                dessin()
                if attemps==0: #perdu
                    endGame("loose", motATrouver)
        else:
            allLetter.append(tryIt)
            searchWord:list = reveler(tryIt, motATrouver, searchWord)
            SearchWord.config(text= listToStr(searchWord))
            InCorrect .config(text= "Correct !", fg= "green")
            Letter    .config(fg= "green")
            if not "*" in searchWord:
                endGame("win", motATrouver)
        del actualLetter
        
    elif pressed in allLetter:
        Letter.config(text="Lettre déjà testé")
        
    elif pressed in letter:
        Letter.config(text=pressed.upper())
        actualLetter = pressed


def game(difficulty, difficultyColor, attempsVar):
    global attemps
    global dessinStatue

    motATrouver  = newWord()
    searchWord   = ["*"]*len(motATrouver)
    print(motATrouver)
    badLetter    = []
    allLetter    = []
    totalAttemps = attemps = attempsVar
    dessinStatue = [1,attempsVar]

    Welcome    .place_forget()
    Difficulty .place_forget()
    Easy       .place_forget()
    Medium     .place_forget()
    Hard       .place_forget()

    #Left
    SearchWord         .config(text= listToStr(searchWord))
    SelectedDifficulty .config(text= "Difficulté : {}".format(difficulty), fg= difficultyColor)

    win.bind_all('<Key>', lambda evt: event(evt, motATrouver, searchWord, badLetter,allLetter, totalAttemps))

    SearchWord.place         (x= 0, y= 100, width= 550, height= 100)
    Hint.place               (x= 0, y= 270, width= 550, height= 25 )
    SelectedDifficulty.place (x= 0, y= 0,   width= 550, height= 95 )
    InCorrect.place          (x= 0, y= 430, width= 550, height= 25 )
    Letter.place             (x= 0, y= 320, width= 550, height= 75 )

    #Right
    canv.place       (x= 550, y= 0)
    canv.create_line (0, 0, 0.1, 500, width= 5)

    CurrentError .config(text="0/{} erreurs".format(totalAttemps))
    CurrentError .place(x= 553, y= 10,  width= 230, height= 30)
    BadLetterHint.place(x= 553, y= 325, width= 350, height= 65)
    BadLetter    .place(x= 553, y= 370, width= 350, height= 120)


#Main menu
def mainMenu():
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
    BadLetter         .config(text= "")
    Letter            .config(text= "")
    canv              .delete(ALL)

    InCorrect.config (text= "")
    Letter   .config (fg= "black")
    
    Welcome.place   (x= 0,   y= 30 , width=900, height=120)
    Difficulty.place(x= 0,   y= 200, width=900, height=100)
    Easy.place      (x= 120, y= 300, width=170, height=160)
    Medium.place    (x= 340, y= 300, width=170, height=160)
    Hard.place      (x= 560, y= 300, width=170, height=160)

#Left
SelectedDifficulty = Label (win, justify="center", font=("Arial","28"))
SearchWord         = Label (win, justify="center", font=("Arial","48"))
Letter             = Label (win, justify="center", font=("Arial","33"))
InCorrect          = Label (win, justify="center", font=("Arial","22"))
EndGame            = Label (win, justify="center", font=("Arial","35"))
Restart            = Button(win, text="Recommencer", justify="center", font=("Arial","35"), bg="#121235", fg="white", command=mainMenu)
WordIs             = Label (win, justify="center", font=("Arial","30"))
Hint               = Label (win, text = "Appuyer sur une lettre puis sur Entrée pour valider", justify="center", font=("Arial","18"))

#Right
canv          = Canvas(win, width = 350, height=500)
CurrentError  = Label (win, font=("Arial","22"))
BadLetterHint = Label (win, text="Mauvaise lettre :", justify="center" ,font=("Arial","28"))
BadLetter     = Label (win, justify="center" ,font=("Arial","24"))

#Main Menu
Welcome    = Label (win, text = "Bienvenue dans le pendu"    , justify="center", font=("Arial","38"))
Difficulty = Label (win, text = "Choisissez votre difficulté", justify="center", font=("Arial","22"))

Easy       = Button(win, text = "8 erreurs", justify="center", font=("Arial","16"), bg="#4975B7", command=lambda:game("Facile"   , "#4975B7", 8))
Medium     = Button(win, text = "6 erreurs", justify="center", font=("Arial","16"), bg="#1A6300", command=lambda:game("Moyen"    , "#1A6300", 6))
Hard       = Button(win, text = "4 erreurs", justify="center", font=("Arial","16"), bg="#FF3701", command=lambda:game("Difficile", "#FF3701", 4))


mainMenu()
win.mainloop()
