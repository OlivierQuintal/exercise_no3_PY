#4.	Faites une fonction palindrome(mot)qui détecte si un mot est un palindrome – un palindrome est un mot qui demeure le même si on l’inverse (ex. radar, kayak, Laval).

def palindrome(mot):
    motInverse = mot[::-1]
    if mot == motInverse:
        return True
    else:
        return False

motEntre = input("Entrez un mot: ")
if palindrome(motEntre):
    print ("Le mot est un palindrome.")
else:
    print ("Le mot n'est pas un palindrome.")