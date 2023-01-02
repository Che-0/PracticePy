#QUe verga son ?

#efectivamente, fui estupidamente vago en el titulo pero es esto

#   def ufh() -> 'anotacion':


def saluda(palabra) -> 'str':   # Ponemos el tipo de dato que retorna o lo que quramos
    return f"Hola {palabra}"


print(saluda.__annotations__)   # -->  {'return': 'str'}


# Se usa para ayudar a las personas a entender tu codigo 