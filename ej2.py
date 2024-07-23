def paridad(entero:int):
    """Revisa la paridad de un numero mediante el resto de la división por 2"""


    if entero % 2 == 0:
        return "El número ingresado es par"
    else: 
        return "El número ingresado es impar"
    
numero = int(input('Ingrese un numero: '))

print(paridad(numero))

#aqui podemos agregar ese ingreso por teclado y usar la fucnion int() para tranforma el numero ingresado
#entero ya que todo lo que ingresa por teclado es string. Ahi les dejo el ejemplo