#1.	Faites une fonction nommée somme(x,y) qui additionne deux nombres passés en paramètres et retourne le résultat.

def somme(x,y):
    return x+y
nombre1 = int(input("Entrez un nombre: "))
nombre2 = int(input("Entrez un autre nombre: "))

resultat = somme(nombre1,nombre2)
print ("Le résultat de l'addition est: ", resultat)