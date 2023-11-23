# Module 'inpoda', Ce module contient toutes les fonctions d'analyses de DataFrame
# Le but de ce module est donc d'encapsuler toutes les fonctions permetant les analyses du cahier des charges de InPoDa

import sys
import os
CheminModule = os.path.dirname(sys.modules['pandas'].__file__)
sys.path.append(CheminModule)


def TopKH(K, DicoH): # Entrée : {K :'int' (si K>0 on aura un tri décroissant, si K<0 on aura un tri croissant)
                     #          DicoH : 'dict' (Dictionnaire contenant tous les Hashtags de la base de données et leur nombre)}
    from pandas import DataFrame
    DFKH = DataFrame(DicoH.items(), columns=['#', 'Nombre de Tweets'])
    if K > 0:
        DFKH = DFKH.sort_values(by='Nombre de Tweets', ascending=False) # On tri le Dataframe selon les valeurs de la deuxième colonne 'RetweetCount' et on precise 'ascending=False' pour l'ordre décroissant
    else:
        DFKH = DFKH.sort_values(by='Nombre de Tweets', ascending=True) # Inversement on tri le DataFrame par ordre Décroissant
    return DFKH.head(abs(K))  # On passe la valeur absolue de K dans la méthode .head() pour s'assurer qu'elle affiche correctement le Top demandé
         # Sortie : 'DataFrame' (de deux colonnes contenant les Utilisateurs mentionnés et le Nombre de fois qu'ils ont été mentionné)


def TopKU(K, DFP):   # Entrée : {K : 'int' (si K>0 on aura un tri décroissant, si K<0 on aura un tri croissant)
                     #          DFP : 'DataFrame' (Le DataFrame principal)}
    from pandas import concat
    Taille = DFP["RetweetCount"].shape
    for i in range(Taille[0]):
        valeur = int(DFP["RetweetCount"].loc[i])  # On converti les 'str' de la colonne "RetweetCount" en entier pour correctement les trier
        DFP["RetweetCount"].loc[i] = valeur       
    DFKU = concat([DFP["Utilisateurs"], DFP["RetweetCount"]], axis=1)
    if K > 0:
        DFKU = DFKU.sort_values(by="RetweetCount", ascending=False) # On tri le Dataframe selon les valeurs de la deuxième colonne 'RetweetCount' et on precise 'ascending=False' pour l'ordre décroissant
    else:
        DFKU = DFKU.sort_values(by="RetweetCount", ascending=True) # Inversement on tri le DataFrame par ordre Décroissant
    return DFKU.head(abs(K))  # On passe la valeur absolue de K dans la méthode .head() pour s'assurer qu'elle affiche correctement le Top demandé
         # Sortie : 'DataFrame' (de deux colonnes contenant les Utilisateurs et le Nombre de fois qu'ils ont tweeté) 


def TopKA(K, DicoA):  # Entrée : {K :'int' (si K>0 on aura un tri décroissant, si K<0 on aura un tri croissant)
                      #          DicoA : 'dict' (Dictionnaire contenant tous les Arobases de la base de données et leur nombre)}
    from pandas import DataFrame
    DFKA = DataFrame(DicoA.items(), columns=['@', 'Nombre de Mentions'])
    if K > 0:
        DFKA = DFKA.sort_values(by='Nombre de Mentions', ascending=False) # On tri le Dataframe selon les valeurs de la deuxième colonne 'Nombre' et on precise 'ascending=False' pour l'ordre décroissant
    else:
        DFKA = DFKA.sort_values(by='Nombre de Mentions', ascending=True) # Inversement on tri le DataFrame par ordre Décroissant  
    return DFKA.head(abs(K))  # On passe la valeur absolue de K dans la méthode .head() pour s'assurer qu'elle affiche correctement le Top demandé
         # Sortie : 'DataFrame' (de deux colonnes contenant les Utilisateurs et le Nombre de fois qu'ils ont été mentionnés) 

def NbPostUtilisateur(Utilisateur, DFP) : # Entrée : {Utilisateur : 'str' (Le Nom de l'utilisateur)
                                          #          DFP : 'DataFrame' (DataFrame principal)}
    Taille = DFP.shape
    for i in range(Taille[0]):
        if DFP["Utilisateurs"].loc[i] == Utilisateur:
            return (Utilisateur, DFP["RetweetCount"].loc[i])  
    return (Utilisateur, 0)   
        # Sortie : 'tuple' (Utilisateur, nombre de Publications)


def NbPostHashtags(hashtag, DicoH): # Entrée : { hashtag : 'str' (Le Hashtag recherché)
                                    #            DicoH : 'dict' (Le dictionnaire des Hastags)}
    if hashtag in DicoH:
        return (hashtag, DicoH[hashtag])
    else:
        return (hashtag, 0) # Sortie : 'tuple' (#, nombre de publications dans lequel il est mentionné)
    

def TweetsUtilisateur(Utilisateur, DFP): # Entrée : { Utilisateur : 'str' (Nom de l'Utilisateur)
                                         #            DFP : 'DataFrame' (DataFrame principal) }
    from pandas import DataFrame
    if Utilisateur[0] != "@":
        Utilisateur = "@" + Utilisateur
    ExpressionR = 'RT ' + Utilisateur
    ListeTweets = []
    Taille = DFP["TweetText"].shape
    for indice in range(Taille[0]):
        Tweet = DFP["TweetText"].loc[indice]
        if (ExpressionR in Tweet) and (Tweet[len(ExpressionR)+2:] not in ListeTweets):
            ListeTweets.append(Tweet[len(ExpressionR)+2:])
        elif (DFP["Utilisateurs"].loc[indice] == Utilisateur):
            ListeTweets.append(Tweet)
    if ListeTweets == []:
        return DataFrame([{"Tweets postés par : " + Utilisateur:"Erreur : Aucun Tweet posté"}])
    else:
        return DataFrame({"Tweets postés par : " + Utilisateur:ListeTweets}) 
     # Sortie : 'DataFrame' contenant les à chaque ligne un tweet de l'utilisateur (Tweet brut) 
     #          (attention l'index des Tweets de DFTU ne correspondent pas à leur index dans DFP)


def TweetsMentionUtilisateur(Utilisateur, DFP): # Entrée : { Utilisateur : 'str' (Nom d'Utilisateur)
                                                #            DFP : 'DataFrame' (DataFrame principal)
    from pandas import DataFrame
    Taille = DFP.shape
    ListeIndiceTweets = []
    for i in range(Taille[0]):
        ListeA = DFP["@"].loc[i]
        if Utilisateur in ListeA:
            ListeIndiceTweets.append(i)
    DFTMU = DataFrame(DFP["TweetText"].iloc[ListeIndiceTweets])
    DFTMU = DFTMU.rename(columns={"TweetText":"Tweets mentionnant : " + Utilisateur})  # On renomme la colonne pour plus de clarté 
    return DFTMU     # Sortie : 'DataFrame' contenant à chaque ligne les Tweets mentionnant l'Utilisateur, 
                                # l'index de chaque ligne correpond à celui du Tweet brut stocké dans DFP 


def UtilisateurMentionHashtag(Hashtag, DFP): # Entrée : { Hastag : 'str' (Hashtag)
                                             #            DFP : 'DataFrame' (DataFrame principal) }
    from pandas import DataFrame
    Taille = DFP.shape
    ListeIndiceTweets = []
    for i in range(Taille[0]):
        ListeH = DFP["#"].loc[i]
        if Hashtag in ListeH:
            ListeIndiceTweets.append(i)
    if ListeIndiceTweets == []:
        return DataFrame([{"Utilisateurs":"Erreur : Votre Hashtag n'existe pas"}])
    else:
        return DataFrame(DFP["Utilisateurs"].iloc[ListeIndiceTweets]) 
              # Sortie : 'DataFrame' contenant à chaque ligne un Utilisateur qui à mentionner le Hashtag dans son tweet, 
              #          l'index correspond à celui de l'Utilisateur dans DFP


def UtilisateurMentionUtilsateur(Utilisateur, DFP):  # Entrée : { Utilisateur : 'str' (Nom d'Utilisateur)
                                                     #            DFP : 'DataFrame' (DataFrame principal)
    from pandas import DataFrame
    Taille = DFP.shape
    for i in range(Taille[0]):
        if DFP["Utilisateurs"].loc[i] == Utilisateur:
            return DataFrame({Utilisateur + " a mentionné :":DFP["@"].loc[i]})   
    return DataFrame([{"Utilisateurs":"Erreur : Votre Utilisateur n'existe pas"}]) 
           # Sortie : 'DataFrame'  


def TestModule():
    return "le module fonctionne"