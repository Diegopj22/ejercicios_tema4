def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info])
        adyac = aux.adyacentes.inicio
        while(adyac is not None):
            arribo_h(aristas, [aux.info, adyac.destino], adyac.info)
            adyac = adyac.sig
        aux = aux.sig
    while(len(bosque) > 1 and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        origen = None
        for elemento in bosque:
            if(dato[0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None
        for elemento in bosque:
            if(dato[1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
                break
        if(origen is not None and destino is not None):
            if(len(origen) > 1 and len(destino) == 1):
                destino = [dato[0], dato[1]]
            elif(len(destino) > 1 and len(origen) == 1):
                origen = [dato[0], dato[1]]
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[0], dato[1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]



















