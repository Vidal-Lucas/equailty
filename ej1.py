def contraseña1(password:str):
    """Revisa si la contraseña pasada por parámetro es igual a una ingresada por el usuario"""

    
    contraseña_ingresante = input("Ingrese la contraseña: ")
    if password == contraseña_ingresante:
        return "Contraseña correcta"
    else:
        return "La contraseña no es la correcta"


#Pondria un ingreso por teclaro aqui afuera y se lo pasaria como parametro a la fucnion
# y que en la funcion solo verifique si lo que se pasa por parametro, que seria la clave
# ingresada por el usuario, es igual a la esperada. La clave que esperan usetedes la pondria
# como una constante