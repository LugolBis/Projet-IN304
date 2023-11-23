# Module 'tweet', Ce module contient toutes les fonctions d'analyses des Tweets
# Le but de ce module est donc d'encapsuler toutes les fonctions permetant d'extraire d'un tweet des analyses précises (#,@,Topics,Sentiment)

import sys
import os
CheminModule = os.path.dirname(sys.modules['textblob'].__file__)   # On extrait de l'ordinateur le chemin du module 'textblob'
sys.path.append(CheminModule)    # On ajoute le chemin en mémoire dans le module


def Hashtags(chaine): # Entrée : 'str' (le Tweet)
    ListeH = []
    SousChaine = chaine.split()
    for elem in SousChaine:
        if elem.startswith('#') and len(elem)>1:
            elem2 = ''
            indice = 1
            while indice < len(elem):
                if (elem[indice] == '_') or (elem[indice].isalnum() == True):
                    elem2 += elem[indice]
                    indice += 1
                else:
                    indice = len(elem)
            ListeH.append(elem[0]+elem2)
    return ListeH   # Sortie : 'list' (la liste des # du Tweet)

def Arobases(chaine): # Entrée : 'str' (le Tweet)
    ListeA = []
    SousChaine = chaine.split()
    for elem in SousChaine:
        if elem.startswith('@') and len(elem)>1:
            elem2 = ''
            indice = 1
            while indice < len(elem):
                if (elem[indice] == '_') or (elem[indice].isalnum() == True):
                    elem2 += elem[indice]
                    indice += 1
                else:
                    indice = len(elem)
            ListeA.append(elem[0]+elem2)
    return ListeA   # Sortie : 'list' (la liste des @ du Tweet)

def Sentiment(Tweet): # Entrée : 'str' (le Tweet)
    from textblob import TextBlob
    blob = TextBlob(Tweet)
    polarite = blob.sentiment.polarity
    if polarite > 0:
        return 'Positif'
    elif polarite < 0:
        return 'Negatif'
    else:
        return 'Neutre'
            # Sortie : 'str' (Le Sentiment du Tweet)
