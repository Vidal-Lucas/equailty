def palindromo(palabra:str):
    
    return palabra == palabra[::-1]

#deberian corregir la funcion y usar alguna funcion que pase o toda la palabra a mayusculas o 
#a minusculas, que ya existen dichas funciones en python y es facil encontrarlas, para asi poder
#comparar bien las palabras ya que asi como esta la funcion si yo ingreso "Neuquen" me retorna falso
#cuando en realidad Neuquen si es un palindromo pero no lo toma porque la primer n es mayuscula