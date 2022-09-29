# Actividad 12 || PCS
import os
import sys

try:
    
    def abrir_fichero(nombre, tipo):
        ruta = os.path.join(os.path.dirname(__file__), nombre)
        return open(ruta, tipo)

    f1 = abrir_fichero('operacions.txt', 'r')
    f2 = abrir_fichero('solucions.txt', 'w')
    lista = f1.readlines()

        
    for i in lista:
        op = i.split(" ")
                
        match op[1]:
            case '+':
                fun = (lambda x,y : int(op[x])+int(op[y])) 
                resultado = (op[0] + " + " + str(op[2]).strip("\n") + " = " + str(fun(0,2)) + "\n")
                f2.write(resultado)
            case '-':
                fun = (lambda x,y : int(op[x])-int(op[y]))
                resultado = (op[0] + " - " + str(op[2]).strip("\n") + " = " + str(fun(0,2)) + "\n")
                f2.write(resultado)
            case '*':
                fun = (lambda x,y : int(op[x])*int(op[y]))
                resultado = (op[0] + " * " + str(op[2]).strip("\n") + " = " + str(fun(0,2)) + "\n")
                f2.write(resultado)
            case '/':
                fun = (lambda x,y : int(op[x])/int(op[y]))
                resultado = (op[0] + " / " + str(op[2]).strip("\n") + " = " + str(fun(0,2)) + "\n")
                f2.write(resultado)
            
except FileNotFoundError :
    print("EL FICHERO NO EXISTE")
    exit

except ValueError :
    print("VALOR INTRODUCIDO ERRONEO")
    exit

except :
    print("ERROR: ", sys.exc_info()[0])
    exit

finally :
    #  CERRAMOS LOS DOS FICHEROS          
    f1.close()
    f2.close()