#8.	Faire un programme qui demande à l'utilisateur d'entrer l'année, le mois et le jour de sa naissance au format AAAA/MM/JJ et qui affiche la date au format 12 janvier 1985.

from datetime import datetime

def dateNaissance(annee, mois, jour):
    a = datetime(annee, mois, jour)
    str1 = a.strftime("%d %B %Y")
    print(str1)

date = input("Entrez votre date de naissance au format AAAA/MM/JJ: ")

date= date.split('/')
annee = int(date[0])
mois = int(date[1])
jour = int(date[2])

dateNaissance(annee, mois, jour)

