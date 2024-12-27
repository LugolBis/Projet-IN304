# Répartition des tâches

### Loïc Desmares
- Extraction des données de la base : élaboration des fonctions permetant la supression des caractère spéciaux, de l'écriture de la Zone d'atterrissage et du DataFrame principal stockant la base de donnée en local. 
- Analyse des données : élaboration des diverses fonctions d'analyse des tweet (hormis la fonction d'extraction du Sentiment).
- Analyse des Topics : élaboration d'une fonction qui extrait la liste des Topics de chaque tweet à l'aide d'un modèle *BERTopic*.
- Complément de la base de donnée : ajout d'Utilisateurs à chaque tweet de la base de données. 
- Fonctionnalités de InPoDa : utilisation des DataFrames et dictionnaires pour réaliser les fonctionnalitées demandées (Top-K #, etc).
- Encapsulage des fonctions d'analyses dans deux classes : **'Tweet'** et **'Inpoda'**.
- Amélioration de l'interface graphique : ajouts de boutons pour obtenir des histogrammes et résolution des problèmes de réception (post deadline).
- Rédaction de la documentation : rédaction de tous les commentaires, des notebook, du github et du diagramme de InPoDa.

Mon rôle à donc été de coder le coeur du projet et la grande majorité des fonctions. J'ai donc codé les fonctions suivantes :
- ```SuprCaracterSpe()```
- class **Tweet** (Hormis ```Sentiment()```)
    - ```__init__(self, chaine='TweetParDéfaut')```
    - ```Hashtags()```
    - ```Arobases()```
    - ```__repr__()```
- class **Inpoda** (la classe et toutes les fonctions qui sont encapsulées dedans)
    - ```__init__(self, Dico=None, DF=None)```
    - ```TopKH()```
    - ```TopKU()```
    - ```TopKA()```
    - ```TopKT()```
    - ```NbPostUtilisateur()```
    - ```NbPostHashtags()```
    - ```NbPostTopics()```
    - ```TweetsUtilisateur()```
    - ```TweetsMentionUtilisateur()```
    - ```UtilisateurMentionHashtag()```
    - ```UtilisateurMentionUtilisateur()```
    - ```Histogramme()```
    - ```__repr__(self)```
- ```ZoneAtterrissage()```
- ```Topics()```
- ```RecupDonneesP()```
- ```DicoHashtags()```
- ```DicoArobases()```
- ```DicoTopics()```
- ```CreationUtilisateurs```
- ```Refresh()```
- **Interface Graphique**
    - ```reception_tweets_utilisateur```
    - ```plotH()```
    - ```plotU()```
    - ```plotA()```
    - ```plotT()```

### Alexia Desfontaines
- Testeuse : réalisation de tests sur la base de données et détection de nombreux "cas spéciaux" à prendre en compte. 
- Élaboration d'une fonction d'analyse de tweet : l'analyse des Sentiments à l'aide du module Textblob.
- Tentatives d'analyse des Topics : élaborations de fonctions de traduction et d'extraction des Topics à l'aide de Spacy. Malheureusement pour des raisons technique de complexité en temps ces solutions n'ont pas été gardées.
- Interface graphique : élaboration de l'interface graphique à l'aide de Gradio.

Le rôle d'Alexia à donc été de détecter les cas non pris en compte au départ par certaines de mes fonctions, l'élaboration de deux fonctions pour extraire les Sentiments et les Topics d'un tweet, ainsi que la réalisation d'une interface graphique. Alexia à donc codé les fonctions suivantes :
- ```Sentiment()``` (Dans la classe **Tweet**)
- **Interface Graphique** 
    - ```afficher_liste()```
    - ```afficher_hashtags()```
    - ```afficher_arobases()```
    - ```afficher_arobases_m()```
    - ```reception_nbposthashtags()```
    - ```reception_tweets_utilisateur()```