from random import randint

#fonction

#liam
def dictionnaire():
    langue_choisi = (input("quelles langues voulez vous ?"))

    tous_mots=[]                                         #  Liste défini comme vide
    langue=False                                         #variable booléenne
    while langue==False:                                   # boucle while cette partie du code change la langue en "fr"
        choix=langue_choisi                 #ou "en" si autre langue  on recommence
        if choix=="fr":
            Pages_Francais  =  open("langues/liste_francais.txt","r")        #  ouvrir en lecture seul le fichier et stockée dans Pages "francais"
            tous_mots =  Pages_Francais.readlines()                     # Tous les mots sont mis dans Tous Mots
            Pages_Francais.close                                    # on referme le fichier
            langue=True
        elif choix=="en":
            Pages_Anglais = open("langues/words.txt","r")
            tous_mots= Pages_Anglais.readlines()
            Pages_Anglais.close
            langue=True
    dico_lettres  =  {}                                 # dictionnaire vide


    for Mots in tous_mots:                          # Mots prend chaque mots indépendament
        for letter in range(len(Mots)-1):
                Mots[letter].lower()
                if( ord(Mots[letter]) >=  97         #prend les lettres entre a et z
                and ord(Mots[letter]) <=  122
                and  ord(Mots[letter+1]) >=  97
                and ord(Mots[letter+1]) <=  122):
                    lettre = Mots[letter]               #lettre prend le Mots à l'indice letter
                    lettre_suivante  =  Mots[letter+1]  # lettre prend le Mots à l'indice letter +1
                    if not lettre in dico_lettres:      # si lettre n'est pas une clé de dico
                        dico_lettres[lettre]  = []      #ajouter la clé en tant que liste vide
                    if  lettre_suivante !=  lettre:     #si la lettre suivante est différente à la lettre ...
                        if not  lettre_suivante in dico_lettres[lettre] :   #... et qu'elle n'est pas déja une valeur de la clé ...
                            dico_lettres[lettre].append(lettre_suivante)    #   ...on ajoute la valeur
    return dico_lettres


#matthéo
def generateur_mdp(dico, nb_lettre):         #on prend en entrer le nb de lettre par mot du mdp
  """in : le dictionnaire et le nombre de lettre du mot géneré
  out : le mot de passe prononcable (voyelle / consonne) aléatoire """

  mot_entier = ""
  nb_mots = int(input("combien de mots voulez vous que votre mot de passe contienne ? "))

  for n in range(nb_mots):
      word = ""                     # on crée une chaine de caractère qui sera le mot

      premiere_lettre = chr(randint(97,122))   #première lettre du mots generé aléatoirement avec 8 lettres dans le dico
      v = True                                 #on verifie si la lettre generé entre a et z est une clé du dictionnaire
      while v == True:
        if premiere_lettre in dico :
          word = word + premiere_lettre #on rajoute la lettre au mot
          v = False
        else :
          premiere_lettre = chr(randint(97,122)) #sinon on la regénère

      voyelle = ["a", "e", "i", "o", "u", "y"] #liste contenant les voyelles pour plus tard (prononciation)

      for i in range(0,nb_lettre-1):            #boucle avec le nb de lettre demander moins 1 car out of range sinon
            autres_lettres = randint(0,len(dico[premiere_lettre])-1) #choisi un indice au hasard dans la liste de la clé du dico de la lettre précedente

            if word[-1] not in voyelle:                #regarde si la dernière lettre du mot n'est pas une voyelle sois la variable premiere_lettre

                while dico[premiere_lettre][autres_lettres] not in voyelle:
                    autres_lettres = randint(0, len(dico[premiere_lettre]) - 1)
                word += dico[premiere_lettre][autres_lettres] #tant que c'est une consonne on tire une lettre au hasard dans la liste de clé de la dernière lettre du mot puis on l'ajoute au mot
            else:

                while dico[premiere_lettre][autres_lettres] in voyelle: #si la lettre générer est une voyelle
                    autres_lettres = randint(0, len(dico[premiere_lettre]) - 1)
                word += dico[premiere_lettre][autres_lettres] #pareil mais on cherche une consonne pour ne pas avoir deux voyelles d'affilées et donc un mot prononcable
            premiere_lettre = word[-1] #on stock la derniere lettre

      mot_entier +=  word
      if nb_mots - n != 1 :                   #boucle pour enlever le dernier tiret
        mot_entier += "-"         #on rajoute un tiret entre les mots si on est pas au dernier tour

      #explication pour la prononciabilité : -on regarde la dernière lettre du mot si c'est une consonne on rajoute une voyelle generé aléatoirement à partir de la liste du dico
      #                                      -                                     si c'est une voyelle on rajoute une consonne ...
      #                                      -                                     on a donc un enchainement consonne voyelle

  return mot_entier   # enfin la fonction renvoie le mdp




#programme principal


print(generateur_mdp(dictionnaire(), 8))

