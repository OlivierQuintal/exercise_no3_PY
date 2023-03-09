# 9.	À partir du programme précédent, affichez l'âge de l'utilisateur.

# Faites un programme qui:
# -	Crée automatiquement un dictionnaire pour chaque poste de travail;
# -	Met ces dictionnaires dans une liste;
# -	Affiche:
# a.	Tous les postes mis à jour durant les derniers 12 mois;
# b.	Tous les postes situés dans le pavillon "A"


# from datetime import datetime
# from datetime import timedelta

# f = open("fichierData.txt")
# fichierLignes  = f.readlines()
# f.close()

# dictPostes = {}
# listePostes = []
# listeDict = []
# cle = ['nomPoste','marque','numeroSerie','localisation','dateMiseAJour']
# for i in range (len(fichierLignes)):
#     ligne = fichierLignes[i].split(',')
#     dictPostes[cle[0]] = ligne[0]
#     dictPostes[cle[1]] = ligne[1]
#     dictPostes[cle[2]] = ligne[2]
#     dictPostes[cle[3]] = ligne[3]
#     dictPostes[cle[4]] = ligne[4]
#     listePostes.append(dictPostes)
# print(dictPostes)
    
from datetime import datetime
from datetime import timedelta

fichier = open("fichierData.txt") 
listeInventaire = []

for ligne in fichier:
    dictInventaire = {}

    listeLigne = ligne.split(",")
    dictInventaire["Nom"] = listeLigne[0]
    dictInventaire["Marque"] = listeLigne[1]
    dictInventaire["NoSerie"] = listeLigne[2]
    dictInventaire["Localisation"] = listeLigne[3]
    dateListe = listeLigne[4].split('\n')
    dateListe = dateListe[0].split('-')
    dateFormatee = datetime(int(dateListe[0]), int(dateListe[1]), int(dateListe[2]))
    dictInventaire["Date"] = dateFormatee

    listeInventaire.append(dictInventaire)


print("Les postes mis à jour dans les douze derniers mois sont: ")
dateDouzeMois = datetime.now() + timedelta(-365, 0, 0)
for item in listeInventaire:
    if item['Date'] > dateDouzeMois:
        print(item['Nom'])

    
print("\nLes postes situés dans le pavillon A sont: ")
for item in listeInventaire:
    if item['Localisation'].find("A") != -1:
        print(item['Nom'])

fichier.close()
