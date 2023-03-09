#2.	2.	Faites une fonction somme2(listeNombres) qui fait la somme de tous les nombres dans la liste passée et retourne le résultat.

def somme2(listeNombres):
    resultat = 0
    for nombre in listeNombres:
        resultat += nombre
    return resultat

liste = [1,2,3,4,5,6,7,8,9,10]
reponse = somme2(liste)
print ("Le résultat de l'addition de la liste est: ", reponse)