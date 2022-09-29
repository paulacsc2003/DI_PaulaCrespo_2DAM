# Actividad 13 || PCS
from random import randint

class Error(Exception) :
    pass

class ErrorEnterMassaMenut(Error):
    pass

class ErrorEnterMassaGran(Error):
    pass

class ErrorNoEsEnter(ValueError):
    pass


aleatorio = randint(0, 100)

while (True):
    numero = int(input("Dime un numero: "))

    try :

        if aleatorio == numero :
            print ("Has descubierto el numero")
            break
        elif aleatorio < numero:
            raise ErrorEnterMassaGran()
        elif aleatorio > numero:
            raise ErrorEnterMassaMenut()
        else:
            raise ErrorNoEsEnter()

    except ErrorEnterMassaMenut: 
        print("El numero es más grande")
    except ErrorEnterMassaGran:
        print("El numero es más pequeño")
    except ErrorNoEsEnter:
        print("No has puesto un numero")