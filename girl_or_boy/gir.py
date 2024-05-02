def girl_or_boy(nombre_usuario):
    # Asumimos que nombre_usuario es una cadena con letras minúsculas como se indica en los requerimientos.
    
    # Comprobaciones iniciales para asegurarse que se siguen los requisitos
    if not nombre_usuario.isalpha() or not nombre_usuario.islower():
        raise ValueError("El nombre debe contener solo letras en minúscula.")

    # Usamos un conjunto para obtener los caracteres únicos.
    chars = set(nombre_usuario)

    # Determinamos el resultado basado en la paridad del número de caracteres distintos.
    if len(chars) % 2 == 0:
        return "¡ITS A GIRL!"
    else:
        return "¡ITS A BOY!"

# Ejemplos de uso de la función
print(girl_or_boy("maria"))  # Ejemplo con un nombre válido.
print(girl_or_boy("jose"))   # Otro ejemplo con un nombre válido.
print(girl_or_boy("ericwithc04"))
print(girl_or_boy("rodriasd"))
print(girl_or_boy("miqueas"))
print(girl_or_boy("miqueas232232"))