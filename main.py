from ej1 import contraseña1
from ej2 import paridad
from ej3 import saludo
from ej4 import *
from ej5 import palindromo
#Main Trabajo Práctico 2 , aca se pondran las pruebas de los ejercicios 

def main():
    contraseña = 'x'
    print(contraseña1(contraseña))
    entero = 2
    print(paridad(entero))
    nombre = 2
    saludo(nombre)
    entero1 = 4
    tabla10(entero1) 
    tabla10_version2(entero1)
    palabra = 212
    print(palindromo(palabra))



if __name__ == "__main__":
    main()
