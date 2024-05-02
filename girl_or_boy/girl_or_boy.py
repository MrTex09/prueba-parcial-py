def girl_or_boy(nombre_usuario):

    # Validaciones
    if type(nombre_usuario) != str:  # noqa: E721
        raise TypeError("El parametro recibido no es una cadena")
    
    if len(nombre_usuario) == 0:
        raise ValueError("El parametro recibido es una cadena vacia")
    
    if not nombre_usuario.isalpha() or not nombre_usuario.islower():
        raise ValueError("El nombre debe contener solo letras en minúscula.")

    try:
        chars = []

        # Se guarda cada caracter en una lista, cada uno solamente una vez
        for i in nombre_usuario:
            if i not in chars:
                chars.append(i)

        # Si es par, es una mujer, si es impar, es un hombre
        if len(chars) % 2 == 0:
            return "¡ITS A GIRL!"
        else:
            return "¡ITS A BOY!"
    except Exception as e:
        return e

# Ejemplos
print(girl_or_boy("ericwithc04"))
print(girl_or_boy("rodriasd"))
print(girl_or_boy("miqueas"))
print(girl_or_boy("miqueas232232"))