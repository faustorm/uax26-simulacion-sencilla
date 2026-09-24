def comprobarDependencia (nombreEdificio, dependencias, listaEdificios = []):
    if not nombreEdificio:
        return False

    dependenciasActual = dependencias[nombreEdificio]
    print(f"Las dependencias para {nombreEdificio} son {dependenciasActual}")

    #comprobamos que cada uno de los edificios está dentro de la lista de edificios construídos
    for d in dependenciasActual:
        #si una no está, yano cumple
        if d not in listaEdificios:
            return False
    return True
    