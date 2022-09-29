# Actividad 11 || PCS
import os

# ABRIMOS LOS FICHEROS
def abrir_fichero(nombre, tipo):
    ruta = os.path.join(os.path.dirname(__file__), nombre)
    return open(ruta, tipo)

f1 = abrir_fichero('operacions.txt', 'r')
f2 = abrir_fichero('solucions.txt', 'w')

# LEEMOS DEL FICHERO DE LAS OPERACIONES
lista = f1.readlines()

       
for i in lista:
    # SEPARAMOS LA LINEA POR CARACTERES
    op = i.split(" ")
            
    # HACEMOS LA OPERACIÓN
    match op[1]:
        case '+':
            fun = (lambda x,y : int(op[x])+int(op[y])) # OPERACION
            resultado = (op[0] + " + " + str(op[2]).strip("\n") + " = " + str(fun(0,2)) + "\n") # LO JUNTAMOS
            f2.write(resultado) # LO PASAMOS AL OTRO FICHERO
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

#  CERRAMOS LOS DOS FICHEROS          
f1.close()
f2.close()