def contraseña1(password:str):
    """Revisa si la contraseña pasada por parámetro es igual a una ingresada por el usuario"""

    
    contraseña_ingresante = input("Ingrese la contraseña: ")
    if password == contraseña_ingresante:
        return "Contraseña correcta"
    else:
        return "La contraseña no es la correcta"

    