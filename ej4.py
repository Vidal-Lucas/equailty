def tabla10(entero:int):
    """Imprime en pantalla la tabla del 10 del parámetro ingresado"""


    for i in range(1,11):
        print(i*entero)
    return 

def input_int():
    """Recibe un valor , si es entero lo devuelve sino pide que se ingrese un nuevo valor"""

    
    while True:
        numero = input("Ingrese otro entero: ")

        try:
            num = int(numero)
            return num
        except ValueError:
            print("Debe ingresar un entero")
            

def tabla10_version2(entero:int):
    """Imprime en pantalla la tabla del 10 del parámetro ingresado y hace lo mismo con 
    nuevos números ingresados por el usuario hasta que uno de ellos sea 0"""


    tabla10(entero)
    num = input_int()
    while num != 0:
        tabla10(num)
        num = input_int()
    return
