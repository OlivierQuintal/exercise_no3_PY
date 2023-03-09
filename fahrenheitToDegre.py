#3.	Faites une fonction toCelsius(nombre) qui convertit les degrés Fahrenheit en degrés Celsius et retourne le résultat.

def toCelsius(degF):
    degC = (degF - 32) * 5/9
    return degC

degreF = int(input("Entrez un nombre degrés Fahrenheit: "))
degreC = toCelsius(degreF)
print ("Le résultat de la conversion est: ", degreC)