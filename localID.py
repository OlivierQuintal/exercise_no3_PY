#4.	Faites une fonction palindrome(mot)qui détecte si un mot est un palindrome – un palindrome est un mot qui demeure le même si on l’inverse (ex. radar, kayak, Laval).

def loginID(nomFamille, prenom, taille1, taille2):
    return nomFamille[0:taille1] + prenom[0:taille2]

nom = input("Entrez votre nom et nom de famille: ")
tailleno1 = int(input("Entrez la taille du nom: "))
tailleno2 = int(input("Entrez la taille du nom de famille: "))

nom = nom.split(' ')

login = loginID(nom[1], nom[0], tailleno1, tailleno2)
print ("Votre login est: ", login)