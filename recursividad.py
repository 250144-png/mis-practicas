def limpiar_feed(publicaciones: list) -> list:
    # Caso base: si tiene 0 o 1 elementos, no puede tener duplicados consecutivos
    if len(publicaciones) <= 1:
        return publicaciones

    # Caso recursivo; compara el primero con el segundo
    if publicaciones[0] == publicaciones[1]:
        # Si son iguales, omite el primero
        return limpiar_feed(publicaciones[1:])
    else:
        # Si son diferentes, conserva el primero
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

# Prueba
print(limpiar_feed(["Post A", "Post B", "Post B", "Post C", "Post B"]))